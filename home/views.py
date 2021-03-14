from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
from home.models import Messages , eventregister, complaintfile, meetingp, mreport
from home.permissions import corebody, executivebody, generalbody, guest
from django.contrib.auth.models import auth, User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is HomePage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is AboutPage")

def team(request):
    # context= {
    #     'variable':"this is sent"
    # }
    #return render(request, 'events.html', context)
    return render(request, 'team.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Messages(name=name, email=email, message=message)
        contact.save()
        messages.info(request,'Your message has been delivered !')

    return render(request, 'contact.html')
    #return HttpResponse("This is ContactPage")

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if password==password1 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists.')
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                guest.append(username)
                messages.info(request,'User has been created.')
                return redirect('/')
        else:
            messages.info(request,'Password didnt match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if request.user.username in corebody:
                return redirect("/admin")
            else:
                return redirect('/')
        
        else:
            messages.info(request, 'Invalid Credentials. Contact the core body if you forgot your credentials.')
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth_logout(request)
    return redirect("/")

def events(request):
    if request.user.username in generalbody or request.user.username in executivebody or request.user.username in corebody:
        if request.method == "POST":
            name=request.POST.get('name')
            mtype=request.POST.get('mtype')
            # tname=request.POST.get('tname')
            title=request.POST.get('title')
            ed=request.POST.get('ed')
            description=request.POST.get('description')
            event=eventregister(name=name, mtype=mtype, title=title, ed=ed, description=description)
            event.save()
            messages.info(request,'Your request has been submitted')
        return render(request, 'events.html')
    else:
        messages.info(request, 'Access Denied')
        return redirect('/')


def complaint(request):
    if request.method == "POST":
        name=request.POST.get('name')
        mtype=request.POST.get('mtype')
        tname=request.POST.get('tname')
        complaint=request.POST.get('complaint')
        comp=complaintfile(name=name, mtype=mtype, tname=tname, complaint=complaint)
        comp.save()
        messages.info(request,'Your complaint has been filed')
    return render(request, 'complaint.html')

def meeting(request):
    if request.user.username in corebody:
        if request.method == "POST":
            name=request.POST.get('name')
            post=request.POST.get('post')
            tname=request.POST.get('tname')
            aud=request.POST.get('aud')
            tnd=request.POST.get('tnd')
            agenda=request.POST.get('agenda')
            meet=meetingp(name=name, post=post, tname=tname, aud=aud, tnd=tnd, agenda=agenda)
            meet.save()
            messages.info(request,'Your meeting request has been submitted')
        return render(request, 'meeting.html')

    elif request.user.username in executivebody:
        if request.method == "POST":
            name=request.POST.get('name')
            post=request.POST.get('post')
            tname=request.POST.get('tname')
            aud=request.POST.get('aud')
            tnd=request.POST.get('tnd')
            agenda=request.POST.get('agenda')
            meet=meetingp(name=name, post=post, tname=tname, aud=aud, tnd=tnd, agenda=agenda)
            meet.save()
            messages.info(request,'Your meeting request has been submitted')
        return render(request, 'meeting.html')
        
    else:
        messages.info(request, 'Access Denied')
        return redirect('/')

def report(request):
    if request.user.username in corebody:
        if request.method == "POST":
            name=request.POST.get('name')
            post=request.POST.get('post')
            tname=request.POST.get('tname')
            mon=request.POST.get('mon')
            report=request.POST.get('report')
            rep=mreport(name=name, post=post, tname=tname, mon=mon, report=report)
            rep.save()
            messages.info(request,'Your monthly report has been submitted')
        return render(request, 'report.html')

    elif request.user.username in executivebody:
        if request.method == "POST":
            name=request.POST.get('name')
            post=request.POST.get('post')
            tname=request.POST.get('tname')
            mon=request.POST.get('mon')
            report=request.POST.get('report')
            rep=mreport(name=name, post=post, tname=tname, mon=mon, report=report)
            rep.save()
            messages.info(request,'Your monthly report has been submitted')
        return render(request, 'report.html')
        
    else:
        messages.info(request, 'Access Denied')
        return redirect('/')