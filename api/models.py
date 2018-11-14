from rest_framework import serializers
from django.db import models
from datetime import datetime
# from django.utils import timezone
import django
from django.core.files import File
from django.contrib.auth.models import AbstractUser

class Group(models.Model):
    name = models.CharField(default="", max_length=50)
    
    def __str__(self):
        return self.name

class GroupSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Group 
        exclude = ()

# Project models here. 
class Image(models.Model):
    image = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}" 

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        exclude = ()


class Category(models.Model):
    ITEM_TYPES = (
        ('Style', 'Style'),
        ('Style', 'Product'),
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=7, choices=ITEM_TYPES, default='P')
    
    def __str__(self):
        return self.name

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class Product(models.Model):
    type = models.CharField(default="Product", max_length=10, editable=False)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    company = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    num_requested = models.IntegerField(default=1)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True, default="")
    date = models.DateField(auto_now_add=True)
    purchased_date = models.DateField(blank=True, auto_now=True) # Added date
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class ProductSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        exclude = ()


class Style(models.Model):
    type = models.CharField(default="Style", max_length=10, editable=False)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    num_requested = models.IntegerField(default=1)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True, default="")
    duration = models.FloatField()
    date = models.DateField(default=django.utils.timezone.now) # Added date
    purchased_date = models.DateField(blank=True, default=django.utils.timezone.now)
    categories = models.ManyToManyField(Category, blank=True, default="")

    def __str__(self):
            return self.name

class StyleSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Style
        exclude = ()


class Cart (models.Model):
    name = models.CharField(max_length=50, default="my cart")
    styles = models.ManyToManyField(Style, blank=True, default="")
    products = models.ManyToManyField(Product, blank=True, default="")

    def __str__(self):
        return self.name

class CartSerializer(serializers.ModelSerializer):
    styles = StyleSerializer(many=True)
    products = ProductSerializer(many=True)

    class Meta:
        model = Cart
        # fields = ('styles', 'products', 'name', 'id' )
        exclude = ()


class Purchased(models.Model):
    name = models.CharField(max_length=50, default="my purchase history")
    styles = models.ManyToManyField(Style, blank=True, default="")
    products = models.ManyToManyField(Product, blank=True, default="")

    def __str__(self):
        return self.name

class PurchasedSerializer(serializers.ModelSerializer):
    styles = StyleSerializer(many=True)
    products = ProductSerializer(many=True)
    
    class Meta:
        model = Purchased
        exclude = ()


class User(AbstractUser):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True, default="")
    # first_name = models.CharField(max_length=25)
    # last_name = models.CharField(max_length=25)
    # username = models.CharField(max_length=25)
    # password = models.CharField(max_length=25)
    # email = models.CharField(max_length=25)
    phone = models.CharField(max_length=18, default="001 (123) 123-1234")
    address = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zipcode = models.IntegerField(blank=True, null=True)
    stylist = models.BooleanField(default=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True, default="") #
    
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, blank=True, null=True, default="")
    purchased = models.OneToOneField(Purchased, on_delete=models.CASCADE, blank=True, null=True, default="")
    
    def __str__(self):
            return f"{self.last_name}, {self.first_name}"  

class UserSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    purchased = PurchasedSerializer()
    cart = CartSerializer()

    class Meta:
        model = User
        exclude = ()


class Stylist(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True, default="")
    type = models.CharField(default="Stylist", max_length=10, editable=False)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=18, default="001 (123) 123-1234")
    address = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zipcode = models.IntegerField(blank=True, default=0, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateField(default=django.utils.timezone.now) # Added date
    
    def __str__(self):
            return f"{self.name}"  

class StylistSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
  
    class Meta:
        model = Stylist
        exclude = ()

class Featurette(models.Model):
    name = models.CharField(max_length=50, default="featurette")
    style = models.OneToOneField(Style, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    stylist = models.OneToOneField(Stylist, on_delete=models.CASCADE, default=1)
    updated_date = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return self.name

class FeaturetteSerializer(serializers.ModelSerializer):
    style = StyleSerializer()
    product = ProductSerializer()
    stylist = StylistSerializer()

    class Meta:
        model = Featurette
        fields = ("stylist","style", "product" )
        exclude = ()

