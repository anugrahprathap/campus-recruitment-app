from django.db import models
from django.contrib.auth.models import User

class company(models.Model):
    name = models.CharField(max_length=100)
    comp_name = models.CharField(max_length=100)
    location = models.CharField(max_length=500)  
    description = models.CharField(max_length=500)
    mobile = models.BigIntegerField()
    mail = models.EmailField( max_length=254)
    linkedin = models.URLField(max_length=200)
    url = models.URLField(max_length=200)
    login_id = models.ForeignKey(User,on_delete=models.CASCADE)
    
