from django.shortcuts import render
from django.http import HttpResponse


def homepage_response(request):
    return render(request,'homepage_templates.html')
