from django.shortcuts import render 
from database.models import *
from django.core.paginator import Paginator

# Create your views here.
def Home ( request ):
     return render(request , 'index.html')
 
 
from  django.db.models import Q , Sum 
def get_student(request ):
     student = Student.objects.all()
     
     if request.GET.get('search'):
          search = request.GET.get('search')
          student = student.filter(
            Q(student_id__student_id__icontains  = search)|
            Q(department__department__icontains =search)|            
            Q(student_email__icontains =search)|          
            Q(student_age__icontains =search)|
            Q(student_name__icontains =search)       
       )          
     paginator = Paginator(student, 25)  # Show 25 contacts per page.
     page_number = request.GET.get("page",1)
     page_obj = paginator.get_page(page_number)

     context = {'students': page_obj}
     return render(request, 'student.html',context)
   
   
def see_report (request, student_id):
     query = Subjects_marks.objects.filter( student__student_id__student_id = student_id)
     
     total_marks = query.aggregate( total_marks= Sum("marks"))
     context={"query": query , "total_marks":total_marks } 
     return render( request, 'report_card.html',context)
   

  