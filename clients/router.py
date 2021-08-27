from django.db import router
from .views import *
from rest_framework import routers
from bills.views import *
from products.views import *
from bills_products.views import *

router = routers.DefaultRouter()
router.register('clients',ClientsViewSet)
router.register('bills',BillsViewSet)
router.register('products',ProductsViewSet)
router.register('bills_products',BillsProductsViewset)