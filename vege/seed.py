from faker import Faker
fake = Faker()
import random

from .models import *

def create_subject_marks(n):
    try:
        student_obj = Student.objects.all()
        for student in student_obj:
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectMark.objects.create(
                    subject = subject,
                    student = student,
                    marks = random.randint(0,100)
                )
    except Exception as e:
        print(e)

def speed_db(n = 10) ->None:
    
    for i in range( 0 ,n):
        department_obj = Department.objects.all()
        random_index = random.randint(0,len(department_obj) -1)
        department = department_obj[random_index]
        student_id = f'stu__0{random.randint(100,999)}'
        
        student_name = fake.name()
        student_email = fake.email()
        student_age = random.randint(20,30)
        student_address = fake.address()
        
        student_id_obj= StudentID.objects.create(student_id=student_id)
        
        student_obj= Student.objects.create(
            
            department =  department,
            student_id = student_id_obj,
            student_name=student_name,
            student_email=student_email,
            student_age=student_age,
            student_address=student_address
        )