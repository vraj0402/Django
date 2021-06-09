from django.http import response
from django.shortcuts import render,HttpResponse
from datetime import datetime
from .models import Contact

# Create your views here.
def index(request):
    context={
        'variable':'this is set',
        'variable2':"variable value is this"
    }
    #return render(request, 'index.html', context)  and in index.html we can access this variables useing {{variable_name}}
    return render(request,'index.html')
    #return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about  page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services page")

def contact(request):
    if request.method == 'POST':
        fname=request.POST.get('f_name')
        lname = request.POST.get('f_name')
        company = request.POST.get('f_name')
        address = request.POST.get('f_name')
        email = request.POST.get('f_name')
        phone = request.POST.get('f_name')
        a_info = request.POST.get('f_name')
        contact = Contact(fname=fname,lname=lname,company=company,address=address,email=email,phone=phone,a_info=a_info,date=datetime.today())
        contact.save()
    return render(request,'contact.html')
    #return HttpResponse("this is contact page")
def result(request):
    context={
    'fname':request.POST['f_name'],
    'lname':request.POST['l_name'],
    'c_name':request.POST['c_name'],
    'add':request.POST['add'],
    'email':request.POST['email'],
    'phone':request.POST['phone'],
    'a_info':request.POST['a_info']
    }

    return render(request,'result.html',context)