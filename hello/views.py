from django.shortcuts import render,HttpResponse,redirect
from hello.models import LoggedIn

MESSAGE_TAGS = {
    'lname':'ramam'
}





# Create your views here.
def index(request):
    return render(request, 'index123.html')

def logged(request):
    global MESSAGE_TAGS
    if request.method == 'POST':
       name2 = request.POST.get('name')
       password2 = request.POST.get('password')
       for i in LoggedIn.objects.all():
           if name2 == i.name and password2 == i.password:
               MESSAGE_TAGS['lname'] = name2
            #    user = form.save()
               return redirect('/home')
    return render(request,'login1.html')

def academy(request):
    return render(request,'academic.html')

def loggedOut(request):
    return HttpResponse('this is the loggedOut page')

def signed(request):
    if request.method == 'POST':
        name1 = request.POST.get('name')
        pass1 = request.POST.get('password')
        # name2 = request.POST.get('')
        log1 = LoggedIn(name = name1,password = pass1,extra1 = "none")

        log1.save()
        return redirect('/')
        
    return render(request,'sign1.html')

def temple(request):
    return HttpResponse('this is the templates page')

def clubs(request):
    return render(request,'clubs12.html')

def sports(request):
    return render(request, 'sports1.html')

def query(request):
    return render(request, 'query1.html')

def event(request):
    return render(request,'event.html')




