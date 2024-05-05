import random
from faker import Faker
from .models import *
faker  = Faker()


def create_marks( n):
 try :
     students=Student.objects.all()
     subjects=Subjects.objects.all()
     for student in students:
         for subject in subjects:
             Subjects_marks.objects.create(
                 
                 student=student,
                 subjects=subject,
                 marks =random.randint(0,100),
                 
             )
 except Exception as e: 
        print(e)
def seed_db(n=100)->None:
    try :
     for _ in range(n):
        
        department_obj = Department.objects.all()
        department =department_obj[random.randint(0 , len(department_obj)-1)]
        student_id =f"STU-0{random.randint(100, 999)}"
        student_name= faker.name()
        student_email = faker.email()
        student_age = random.randint(20, 30 )
        
        student_address = faker.address()
        student_id_obj= StudentID.objects.create(student_id= student_id)
        student_obj = Student.objects.create(
            
            department= department,
            student_id= student_id_obj,
            student_name= student_name,
            student_email= student_email,
            student_age= student_age,
            student_address= student_address,
            
        )
        
    except Exception as e:
           print (e)
          