from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserRegister(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    door_no = models.PositiveIntegerField()
    street = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    userpic = models.ImageField(upload_to='profiles/',blank=True,null=True)