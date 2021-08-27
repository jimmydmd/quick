from django.db import models
from clients.models  import *
# Create your models here.

class Bills(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Clients,
                                on_delete=models.CASCADE,
                                related_name='rel_client_bills')
    company_name = models.CharField(max_length=200, null=True)
    nit = models.IntegerField(null=False)
    code = models.IntegerField(null=False)