from django.contrib import admin
from django.urls import path ,include
from home.views import *
import home.urls 
 

urlpatterns = [
    
    path('',  get_student , name = 'Home'),
    path('student/',get_student, name='get_student'),
    path('see_report/<student_id>/',see_report, name='see_report'),

    
]