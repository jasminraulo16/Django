from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    ceo = models.CharField(max_length=100)
    est_year = models.IntegerField()
    origin = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos', blank=True,null=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company,related_name='companies',on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    seat_capacity = models.IntegerField()
    product_img = models.ImageField(upload_to='products',blank=True,null=True)





