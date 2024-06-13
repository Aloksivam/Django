from unicodedata import name
from django.db import models

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=100)
    cuisine=models.CharField(max_length=80)
    fee=models.IntegerField()
    def __str__(self):
        return self.name+ " : "+self.cuisine

class DrinksCategory(models.Model):
    category_name=models.CharField(max_length=200)
class Drinks(models.Model):
    drink=models.CharField(max_length=200)
    price=models.IntegerField()
    category_id=models.ForeignKey(DrinksCategory,on_delete=models.PROTECT,default=None)

class Demoformer(models.Model):
    name=models.CharField(max_length=100)
    # name=models.CharField(widget=models.Textarea)
    # name=models.CharField(widget=models.Textarea(attrs={'rows':5}))
    email=models.EmailField()
    reserv_date=models.DateField() #widget=models.NumberInput(attrs={'type':'date'})
    def __str__(self):
        return self.name+ " : "+self.name