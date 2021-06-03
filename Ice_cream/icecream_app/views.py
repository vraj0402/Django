from django.shortcuts import render,HttpResponse

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
    return render(request,'contact.html')
    #return HttpResponse("this is contact page")