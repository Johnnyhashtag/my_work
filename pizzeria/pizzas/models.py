from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.

class Pizza(models.Model):

    """A Model of Pizza"""
    name = models.CharField(max_length = 200)

    def __str__(self):
        
        """ A String representation of Pizza model"""
        return self.name

class Topping(models.Model):

    """ A model of pizza toppings. """
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):

        """A String representation of topping model"""
        return self.name