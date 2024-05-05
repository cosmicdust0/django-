from django.shortcuts import render , redirect
from django.views.decorators.csrf import csrf_protect
from .models import * 
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url=("/login/"))
@csrf_protect
# Create your views here.
def receipes ( request):
    if request.method == "POST":
     data = request.POST
     image = request.FILES.get("receipe_image")  
     name = data.get("receipe_name")    
     des = data.get("receipe_des")    
   
     
     Receipes.objects.create(
        receipe_name =name,
        receipe_des = des,
        receipe_image= image,
     )
     
     return redirect('/receipes/')
  
    receipes_list = Receipes.objects.all()
    check = request.GET.get('search')
    if check:
      receipes_list= receipes_list.filter(receipe_name__icontains = check)
    context= {'receipes':receipes_list}
    return render( request , "receipes.html", context)
 
@login_required(login_url=("/login/"))
def update_receipe( request , id):
   data = Receipes.objects.get(id = id )
   context={'receipe':data}
   
   if request.method == 'POST':
    query=request.POST
    
    data.receipe_name=query.get("receipe_name")
    data.receipe_des=query.get("receipe_des")
    
    if request.FILES.get("receipe_image"):
     data.receipe_image=request.FILES.get("receipe_image")
    
    
    data.save()
    return redirect('/receipes/')
   return render( request , "update_receipe.html", context)
    
   
   
@login_required(login_url=("/login/"))

def delete_receipe( request , id):
   
   data = Receipes.objects.get(id = id )
   data.delete()
   return redirect('/receipes/')


def login_page(request):
   if request.method =='POST':
    data = request.POST
    username = data.get('Username')
    password = data.get('password')
    
    if not User.objects.filter(username=username).exists():
        messages.info( request , "Invalid username")
        return redirect( "/login/")
    user = authenticate(username = username , password= password)
    if user is None:
       messages.info(request, " Invalid password")
    else:
        login( request,user) 
        return redirect('/receipes/') 
   return render ( request, "login.html")

@login_required(login_url=("/login/"))
def logout_page(request):
   logout(request)
   return redirect('/login/') 
 
def register_page(request):
    if request.method =='POST':
        data = request.POST
        username = data.get('Username')
        password = data.get('password')
        
        user= User.objects.filter(username=username)
        if user.exists():
          messages.info( request , "Username already taken ")
          return redirect("/register/") 
           
        user = User.objects.create(
            username=username,
           
        )
        user.set_password(password)
        user.save()
        messages.info( request , "Account created successfuly ")
        return redirect("/register/")
    
    return render ( request, "register.html")
 
#  vege= Receipes.objects.all().order_by('receipe_count')
#ascending  vege= Receipes.objects.all().order_by('receipe_count')[0:2]
#desecnding  vege= Receipes.objects.all().order_by('-receipe_count')[0:2]

# view the no. of items greater than or less than a given count 
#desecnding  vege= Receipes.objects.all().filter(receipe_count__gte = 55)
#  here __ indicate spl str that django will indetify and replace ex here gte is greate than or equal to 



