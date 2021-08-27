from django.db import models

class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.IntegerField(null=False)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=False)