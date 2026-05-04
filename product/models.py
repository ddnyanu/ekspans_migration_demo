from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    category= models.CharField(max_length=255,blank=True,null=True)
    type= models.CharField(max_length=255,blank=True,null=True)
    
    class Meta:
        db_table = "product_data"

    def __str__(self):
        return self.name