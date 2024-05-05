from django.contrib import admin
from django.urls import path ,include
from home.views import *
import home.urls 
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('home.urls'), name = 'Home')
]
