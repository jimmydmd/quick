from django.urls import include, path
from rest_framework import routers
from clients import views
from django.contrib import admin
from clients.router import router
from django.conf.urls import url
from users.views import *


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('export/', views.export),
    path('import/', views.upload_csv)
]
