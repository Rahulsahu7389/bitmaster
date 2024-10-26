from django.shortcuts import render,HttpResponse
from hello.models import LoggedIn





# Create your views here.
def index(request):
    return HttpResponse('this is the index page')

def logged(request):
    return HttpResponse('this is the logged page')

def academy(request):
    return HttpResponse('this is the academy page')

def loggedOut(request):
    return HttpResponse('this is the loggedOut page')

def signed(request):
    # if request.method == 'POST':
    #     name1 = request.POST.get('name')
    #     pass1 = request.POST.get('password')
        
    return render(request,'sign1.html')

def temple(request):
    return HttpResponse('this is the templates page')

def clubs(request):
    return HttpResponse('this is the clubs page')

def sports(request):
    return HttpResponse('this is the sports page')

