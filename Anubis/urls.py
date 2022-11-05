from django.contrib import admin
from django.urls import path
from anubis.views import homePage, fileUpload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage'),
    path('file-upload', fileUpload, name='fileUpload')
]
