from django.shortcuts import render, HttpResponse

def homePage(request):
    return HttpResponse("Hello Anubis")
