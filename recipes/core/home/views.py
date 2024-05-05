from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home ( request ):
    
    peoples = [
        { 'name':'Ravi' , 'age':26},
        { 'name':'Bhima' , 'age':26},
        { 'name':'yash' , 'age':26},
        { 'name':'Pranv' , 'age':17},
        { 'name':'pratiksha' , 'age':26},
        
    ]
    vegetables =[ 'tomato', 'capsicum', 'carrot'
    ]   
    return render( request, 'index.html', context={'one':peoples, 'vegs': vegetables})
 
def about ( request ):
     return  render ( request , "about.html")
 
def contact ( request ):
     return  render ( request , "contact.html")


def success_page (request ):
      return HttpResponse("<h1> Hi page successfully loaded </h1>")