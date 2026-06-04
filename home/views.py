from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# def home(request):
#     return HttpResponse("<h1>hey i am Django server</h1>")

def home(request):
    
    
    peoples=[
        
        {'name':'Gaurav pandey','age':20,'book':'the maths'},
        {'name':'Shreyans Pandey','age':19,'book':'the Gk in jr class'},
        {'name':'Ramkrishna Pandey','age':45,'book':'Histroy'},
        {'name':'Aarti Pandey','age':36,'book':'the maths'},
        {'name':'shubhi Pandey','age':21,'book':'how become a topper'},
        {'name':'prachi Pandey','age':17,'book':'learning'},
    ]
    
    
    vegetable=['pumpkin','Tamato','Potatoe']
    for people in peoples:
        print(people)
    
    return render(request , "index.html" , context={ 'page':'Django 2026 learner','peoples':peoples ,'vegetables':vegetable})
def about(request):
    context={'page': 'About'}
    return render(request , "about.html" , context)


def contact(request):
    context={'page': 'Contact'}
    return render(request , "contact.html",context)



def success_page(request):
    return HttpResponse("<h1> hey this is  a succes page</h1>")
    