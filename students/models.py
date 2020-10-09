from django.db import models
from django.forms import ModelForm, Textarea


# Create your models here.

class Students(models.Model):         #yaha Students chai model ko naaam ho
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

class Meta:
    db_table = "students"      # table ko naam students rakheko



