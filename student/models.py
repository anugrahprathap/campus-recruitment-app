from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from faculty.models import event
# Create your models here.



class student(models.Model):
    name = models.CharField(max_length=100)
    cgpa = models.FloatField()
    resume = models.FileField(blank=True)
    mobile = PhoneNumberField(null=False, blank=False, unique=True)
    course = models.CharField(max_length=100)
    stu_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
class eventcon(models.Model):
    event_id = models.ForeignKey(event, on_delete=models.CASCADE)
    student_id = models.ForeignKey(student, on_delete=models.CASCADE) 
    status = models.CharField(max_length=50,default='pending')
    
class result(models.Model):
    stu_id = models.ForeignKey(student,on_delete=models.CASCADE)
    event_id = models.ForeignKey(event,on_delete=models.CASCADE)
    publish_date = models.DateField()
    

    