from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html') #TODO: Arreglar esto

def healthCheck(request):
    return HttpResponse("ok")