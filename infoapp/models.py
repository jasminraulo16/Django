from django.db import models

# Create your models here.
class userDetails(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    userpic = models.ImageField(upload_to='userimg/',blank=True,null=True)