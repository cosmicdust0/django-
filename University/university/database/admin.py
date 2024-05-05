from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Department)
admin.site.register(StudentID)
class Subjects_marks_admin ( admin.ModelAdmin):
    list_display =  ['student','subjects','marks']

admin.site.register(Student)
admin.site.register(Subjects)
admin.site.register(Subjects_marks,Subjects_marks_admin)
