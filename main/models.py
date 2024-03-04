from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255) # Consider using a password hasher for security

class Food(models.Model):
    name = models.CharField(max_length=255)
    calories = models.IntegerField()
    # Add additional nutritional information (optional)

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Calorie(models.Model):
    name = models.CharField(max_length=255)
    calories = models.IntegerField()