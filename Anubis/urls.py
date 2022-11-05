from django.contrib import admin
from django.urls import path
from anubis.views import homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name='homePage')
]
