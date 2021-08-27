from django.db import models

# Create your models here.
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
