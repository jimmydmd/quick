from django.db import models
from bills.models import *
from products.models import *


class BillsProducts(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bills,
                                on_delete=models.CASCADE,
                                related_name='rel_bills_billsproducts')
    product_id  = models.ForeignKey(Products,
                                on_delete=models.CASCADE,
                                related_name='rel_products_billsproducts')
