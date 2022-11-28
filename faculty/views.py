import datetime
import json
from sre_constants import MAGIC
from django.shortcuts import render
from datetime import date

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from student.forms import UserRegForm
from .decorators import unauth_user,allowed_users
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from faculty.decorators import allowed_users
from .models import event,pcoAdd
from company.models import company
from student import views
from student.models import student,eventcon,result
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

def home(request):
    events =event.objects.all()
    context = {
    'events': events,
    }
    return render(request, "faculty/home.html",context)



def stats(request):
    
    
    return render(request, 'faculty/stats.html')



#*****************Login********************
def login_page(request):
    events =event.objects.all()
    context = {
    'events': events,
    }
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        print(user)
        if user is not None:
            login(request, user)
            
            a=Group.objects.all()
            print(a)
            type = request.user.groups.all()
            for id in a:
                print(id)
          
            if type is not None:
                if(type[0] == a[0]):
                    return redirect('pcoHome')
                if(type[0] == a[1]):
                    
                    return redirect('cmphome')
                if(type[0] == a[2]):
                    return redirect('stu_home')
                if(type[0] == a[3]):
                    
                    return redirect('crshome')
                if(type[0] == a[4]):
                    return redirect('pendingCom')
                
                else:
                    
                    return render(request, 'faculty/login.html')
        else:
            messages.info(request,"User name or password is incorrect")
    
    return render(request, 'faculty/login.html')


def logout_user(request):
    logout(request)
    return redirect('complogin')



# **************admin******************

@login_required
@allowed_users(allowed_roles=['admin'])
def admin_home(request):
    return render(request,'faculty/admin/admin_home.html')


@login_required
@allowed_users(allowed_roles=['admin'])
def approveCom(request):
    
    users = User.objects.filter(groups=5)
    data = users.values('id')
    
    com = []
    for row in data:
        com.append(company.objects.get(login_id=row['id']))
    
    context={
        "value" : com
    }
    
    if request.method == 'POST':
        comid = request.POST['comid']
        print(Group.objects.all())
        pending = Group.objects.get(id=5)
        if request.POST['action'] == 'accpect':
            g = Group.objects.get(name='comp')
            users = User.objects.get(username=comid)
            print(users.password)
        
            pending.user_set.remove(users)
            g.user_set.add(users)
           
            messages.success(request,"Company Approved Successfully")
            return redirect('approveCom')
        else:
            g = Group.objects.get(name='rejected')
            users = User.objects.get(username=comid)
            pending.user_set.remove(users)
            g.user_set.add(users)
            return redirect('approveCom')
            
    
    return render(request,'faculty/admin/verifycomp.html',context)


@login_required
@allowed_users(allowed_roles=['admin'])
def addPco(request):
    if request.method == 'POST':
        uname = request.POST['name']
        number =request.POST['number']
        mail =request.POST['mail']
        password = make_password(request.POST['pass'])
        if User.objects.filter(username=uname).count():
            messages.error(request, f'Account details allready exists')
        else:
            
            
            user = User(username=uname,password=password)
            user.save()
            id = User.objects.get(username=uname)
            print(id)
            add = pcoAdd(name=uname,mobile=number,mail=mail,login_id=id)
            add.save()
            a=pcoAdd.objects.all()
            print(a)
            g = Group.objects.get(name='pco')
            users = User.objects.get(username=uname)
            g.user_set.add(users)
            messages.success(request, f'Account Details Updated ')
            return redirect('crshome')  
    
    else:
      
        form = UserRegForm()     
    return render(request, 'faculty/admin/add_pco.html')

@login_required
@allowed_users(allowed_roles=['admin'])

def viewPco(request):
    
    # pco = User.objects.filter(groups__name='pco')
    pco = pcoAdd.objects.all()
    context = {
    'pco': pco,
    }
    print(pco)
    print(context)
    return render(request, 'faculty/admin/viewPco.html',context )
@login_required
@allowed_users(allowed_roles=['admin'])
def viwecom(request):
    com = User.objects.filter(groups=2).select_related()
    data = com.values('id')
    print(data)
    com1 =[]
    for row in data:
        print(row['id'])
        com1.append(company.objects.get(login_id=row['id']))
        
    print (com1)
    return render(request,'faculty/admin/viewcom.html',{'com':com1})
@login_required
@allowed_users(allowed_roles=['admin'])
def adminstats(request):  
    return render(request,'faculty/admin/stats.html')

#*****************PCO**************

@login_required
@allowed_users(allowed_roles=['pco'])
def pco(request):
    return render(request, 'faculty/pco/pcoHome.html')




@login_required
@allowed_users(allowed_roles=['pco'])
def addEvent(request):
    comp  = User.objects.filter(groups=2)
    mdyata = comp.values('id')
    com =[]
    for row in mdyata:
        com.append(company.objects.get(login_id=row['id']))
    
    
    
    if(com):
        data = {
        "value": com,
         }
    else:
        data = {
        "value": None,
         }
    if request.method == 'POST':
        ename = request.POST['evtname']
        date1 = request.POST['date']
        cgpa = request.POST['cgpa']
        remarks =request.POST['remarks']
        comp = request.POST['comp']
        print(date1)
        today =date.today()
        date2 =datetime.datetime.strptime(date1, "%Y-%m-%d").date()
        if date2 >today:
            companys = company.objects.get(id=comp)
            user = pcoAdd.objects.get(login_id = request.user)
            eventadd=event(eventname=ename,date=date,cgpa=cgpa,remarks=remarks,comp=companys,pco_id=user)
            eventadd.save()
            messages.success(request, f'Event { ename } Created at { date } ')
        else:
            messages.success(request,f'Select A valid date')
    
    return render(request, 'faculty/pco/addEvent.html',data)

@login_required
@allowed_users(allowed_roles=['pco'])
def viewEvent(request):
    events = event.objects.all()
    context = {
    'events': events,
    }
    
    return render(request , 'faculty/pco/viewEvent.html',context)


def viewStudent(request):
    
    events = event.objects.all()
    value ={
        "value" : events
    }
    context = {
        
    }
    
    if request.method == "POST":
        
        event_id = request.POST['eneme']
        
        ename = event.objects.get(id=event_id)
        con = eventcon.objects.filter(event_id = ename)
        data = con.values('student_id')
        stu = []
        
       
       
        for row in data:
            
            stu.append(student.objects.get(id = row['student_id']))
            print(student.objects.get(id = row['student_id']).id)
        
        
        context = {
            
            'myval' : stu
        }
        print(context['myval'])
        
        
        return render(request, 'faculty/pco/viewstu.html',context)
        
    
    # eventcons = eventcon.objects.filter(student_id=stuid)
    return render(request, 'faculty/pco/viewstu.html',value )



def addplaced(request):
    events = event.objects.all()
    
    if request.method == 'POST':
        if (request.POST['button']=='selevent'):
            
            event_id = request.POST['eneme']
            if event_id !='':
                con = eventcon.objects.filter(event_id=event_id).select_related()
                
                return render(request, 'faculty/pco/addplaced.html',{'students': con,'event':event_id} )
                
        if(request.POST['button']=='submit'):
            
            event_id = request.POST['event_id']
            con = eventcon.objects.filter(event_id=event_id)
            data = con.values('student_id')
            date=datetime.datetime.now()
            name = ''
            for row in data:
                # studentid=student.objects.get(id = row['student_id'])
                val = row['student_id']
                if 'check' in request.POST:
                    event_id = request.POST['event_id']
                    events = event.objects.get(id=event_id)
                    name = events.eventname
                    myid = request.POST['check']
                    print(myid)
                    print(row['student_id'])
                    studentid=student.objects.get(id=row['student_id'])
                    evt =eventcon.objects.get(student_id=studentid,event_id=event_id)
                    evt.status = 'Selected'
                    evt.save()
                else:
                    event_id = request.POST['event_id']
                    evt =eventcon.objects.get(student_id= row['student_id'],event_id=event_id)
                    name = event.objects.get(id=event_id)
                    name = name.eventname
                    evt.status = 'Not_Selected'
                    evt.save()
                
                
            messages.success(request,'Result added Sucessfully')
            events = event.objects.all()
            return render(request, 'faculty/pco/addplaced.html',{'value' : events} )
    return render(request, 'faculty/pco/addplaced.html',{'value' : events} )

def searchstu(req,id):
    if req.method =="POST":
        str2 = json.loads(req.body).get('searchtext')
        con = eventcon.objects.filter(event_id=id).select_related()
        val1 = (con.values("student_id"))
        stud = student.objects.filter(name__istartswith=str2)
        data= stud.values()
        flag =0
        data1 = stud.values('id')
        for row in data1:
            flag = 0
            for row1 in val1:
                
                if (row['id']==row1['student_id']):
                    flag =1         
            if(flag==0):
                stud = stud.exclude(id=row['id'])
        data= stud.values()
        return JsonResponse(list(data), safe=False)

def placedstu(request):
    events = event.objects.all()
    
    if request.method == 'POST':
        
            
        event_id = request.POST['eneme']
        if event_id !='':
            con = eventcon.objects.filter(event_id=event_id,status='Selected').select_related()
            data = con.values('status')
        
        

            return render(request, 'faculty/pco/viewplaced.html',{'students': con} )
    return render(request, 'faculty/pco/viewplaced.html',{'value':events})

@login_required
@allowed_users(allowed_roles=['pco'])
def pcostats(request):  
    return render(request,'faculty/pco/stats.html')
                
      
            
            
            