from django.db import models
    
from django.contrib.auth.models import User
from company.models import company


class pcoAdd(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    mail = models.EmailField( max_length=254)
    login_id = models.ForeignKey(User,on_delete=models.CASCADE)
    

class event(models.Model):
    eventname = models.CharField(max_length=100)
    date = models.DateField()
    cgpa = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.TextField(max_length=500)
    comp = models.ForeignKey(company,on_delete=models.CASCADE)
    pco_id = models.ForeignKey(pcoAdd , on_delete=models.CASCADE)
    
    

class stats(models.Model):
    comp = models.ForeignKey(company,on_delete=models.DO_NOTHING)
    stunum = models.IntegerField()
    batch = models.DateField()
    
# class course(models.Model):
#     courseName = models.CharField(max_length=100)
#     type =  ( ('Regular', 'Senior'),
#         ('Inetgrated', 'Inetgrated'),
        
#     )
