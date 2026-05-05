from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

def index_view(request):
    return HttpResponse("<h1>home page</h1>")

def about_view(request):
    return HttpResponse("<h1>About page</h1>")

def contact_view(request):
    return HttpResponse("<h1>Contact page</h1>")


