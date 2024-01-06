"""Views for the challenges app.
views here will be called according to the urls.py of this app."""

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("January")
