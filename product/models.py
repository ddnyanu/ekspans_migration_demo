from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    
    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name