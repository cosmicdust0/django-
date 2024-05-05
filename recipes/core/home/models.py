from django.db import models



# CRUD 
# creat - class.objects.create(attributes)

#read - car = class.objects.all() or  class.objects.get(id=eg) or class.objects.filter(id=eg) 

#update - object= class.objects.get(id=)
    # object.name= new name 
    # object.year= new year 
    # or class.objects.filter(id= ).update(name= new name )
#  delete operation 
    #  class.objects.get(id).delete()
    #class.objects.all().delete()



# Create your models here.
class Students ( models.Model):
 name= models.CharField( max_length=50)
 age =  models.IntegerField(null=True)
 email = models.EmailField(max_length=254)
 address = models.TextField()

class Car ( models.Model):
    name= models.CharField( max_length=50)
    year = models.IntegerField()
    
    def __str__(self) -> str:
       return self.name