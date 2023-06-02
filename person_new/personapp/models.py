from django.db import models
from django import forms

# Create your models here.

class Person(models.Model):
    first_name=models.CharField(max_length=256)
    last_name=models.CharField(max_length=256)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', ]