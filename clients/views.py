import csv, io
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from clients.serializers import *
from . import models
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView
from bills.models import *
from django.contrib import messages
from django.urls import reverse
from django import forms

class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    permission_classes = [permissions.IsAuthenticated]

def export(request):
    
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['document','First Name', 'Last Name', 'Email', 'Bill Id', 'Company name'])
    
    data_client = Clients.objects.all()
    data_bills = Bills.objects.all()
    print(data_client)
    for cli in data_client:
        for bil in data_bills:
            if bil.client_id_id == cli.id:
                id_bil = bil.id
                company_name = bil.company_name
                client = [cli.document,cli.first_name, cli.last_name, cli.email, id_bil , company_name]
                writer.writerow(client)

    response['Content-Disposition'] = 'attachment; filename="clients.csv"'

    return response



def upload_csv(request):
    template = "clients/csv_upload.html"
    prompt ={
        'order' : 'Order of the CSV should be document, first_name, last_name, email'
    }
    
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file')
        
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Clients.objects.update_or_create(
            id = column[0],
            document = column[1],
            first_name = column[2],
            last_name = column[3],
            email = column[4]
        )
    context={}
    return render(request, template, context)
