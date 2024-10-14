from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.conf import settings

def home(request):
    return render(request, 'home.html')