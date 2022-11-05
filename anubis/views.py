from django.shortcuts import render, HttpResponse

def homePage(request):
    return render(request, "index.html")

def fileUpload(request):
    return render(request, "fileupload.html")