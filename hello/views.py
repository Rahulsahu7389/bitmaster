from django.shortcuts import render,HttpResponse,redirect
from hello.models import LoggedIn,Questions,Templeate,Answer
from json import dumps
from django.core.mail import send_mail

def index(request):
    # send_mail(
    # "Subject here",
    # "Here is the message.",
    # "masterbit165@gmail.com",
    # ["jaysahu0201@gmail.com"],
    # fail_silently=False,)
    return render(request,'index123.html')

MESSAGE_TAGS = {
    'lname':'ramam'
}

def button(request):
    send_mail(
    "Subject here",
    "team : shourya\ntime:12:15pm\ndate:10/27/24\nlocation:amul parlour",
    "masterbit165@gmail.com",
    ["jaysahu0201@gmail.com"],
    fail_silently=False)
    print('got it')
    return redirect('/sports')






# Create your views here.
# def index(request):
#     return render(request, 'index123.html')

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



def clubs(request):
    return render(request,'clubs12.html')

def sports(request):
    return render(request, 'sports1.html')

def query(request):
    context = {}
    qns = Questions.objects.all()
    for i in qns:
        context['qns'] = i.questn
        context['qnsId'] = '3'
        context['qname'] = i.qname

    temp = Templeate.objects.all()
    for j in temp:
        context['year'] = j.year 
        context['branch'] = j.branch
        context['tname'] = j.name

    datajson = dumps(context)

    # ans = Answer.objects.all()
    # for k in ans:
    #     context['answer'] = k.qustn
    #     context['AId'] = k.qustnId
    print(context)
    
    return render(request, 'query1.html',{'data':datajson})

def event(request):
    return render(request,'event.html')

def formed(request):
    global MESSAGE_TAGS
    if request.method == 'POST':
        year1 = request.POST.get('name')
        branch2 = request.POST.get('branch')
        temp = Templeate(year = year1,branch = branch2,name = MESSAGE_TAGS['lname'], extra3 = 'none' )
        temp.save()
        return redirect('/query')
    return render(request,'form.html')
def answered(request):
    if request.method == 'POST':
        ques = request.POST.get('text')
        dat1 = Questions.objects.all()

        ans = Answer(qustn = ques , qustnId = len(dat1), extra4 = 'none')
        ans.save()
        return render(request,'answers1.html')
        # quesId = request.POST.get('')


    context2 = {}
    qns = Questions.objects.all()
    temp = Templeate.objects.all()
    i = 0
    while i < len(qns):
        for j in temp:
            context2[f'data{i}'] = [qns[i].questn,qns[i].questnId,qns[i].qname,j.year,j.branch,j.name]
        i += 1
    datajson = dumps(context2)

    
    return render(request,'answers1.html',{'data':datajson})





