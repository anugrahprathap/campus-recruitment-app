from django.shortcuts import render, redirect
from .models import student, eventcon,result
from django.contrib import messages

from faculty.decorators import allowed_users
from .forms import UserRegForm
from django.contrib.auth.decorators import login_required
from company.models import company
from django.contrib.auth.models import User
from faculty.decorators import allowed_users
from django.contrib.auth.models import Group
from faculty.models import event
from django.core.files.storage import FileSystemStorage
from django.urls import path
from django.db import connection



def stu_register(request):
    
    if request.method == 'POST':
       
        form = UserRegForm(request.POST,request.FILES)
        if form.is_valid():
            print("valid")
            form.save()
            regno = form.cleaned_data.get('username')
            # passw = form.cleaned_data.get('password')
            course = request.POST.get('course')
            g = Group.objects.get(name='stu')
            users = User.objects.get(username=regno)
            g.user_set.add(users)
            Full_Name=form.cleaned_data.get('Full_Name')
            print (Full_Name)
            cgpa = form.cleaned_data.get('cgpa')
            resume = request.FILES['resume']
            
            fss = FileSystemStorage()
            file = fss.save(resume.name, resume)
            file_url = fss.url(file)
            mobile = form.cleaned_data.get('mobile')
            stud = student()
            print(course)
            stud.name = Full_Name
            stud.stu_id = users
            stud.cgpa = cgpa
            stud.resume = file_url
            stud.mobile = mobile
            stud.course = course
            print(course)
            stud.save()
            messages.success(request, f'Account Created for { Full_Name }')
            return redirect('my-home')
        else :
            return render(request,'student/stu_register.html', {'form':form})
        
    else:
      
        form = UserRegForm()
    return render(request,'student/stu_register.html', {'form':form})




@login_required
@allowed_users(allowed_roles=['stu'])
def Stuview(request):
    events =event.objects.all()
    context = {
    'events': events,
    }
    return render(request, 'student/viewevent.html',context)

@login_required
@allowed_users(allowed_roles=['stu'])
def stu_home(request):
    events =event.objects.all()
    context = {
    'event': events,
    }
  
    return render(request, 'student/stu_home.html',context)


@login_required
@allowed_users(allowed_roles=['stu'])
def stuProfile(request):
    user=request.user
    id = User.objects.get(id=user.id)
    
    try:
        data = student.objects.get(stu_id=id)
    
    
    except student.DoesNotExist:
        data = None
   
    if data:
        context = {
            'data': data,
            }
        if request.method == 'POST':
            FullName = request.POST['name']
            cgpa = request.POST['cgpa']
            file = request.FILES.get('resume')
            
            fss = FileSystemStorage()
            file = fss.save(file.name, file)
            file_url = fss.url(file)
            
            number =request.POST['number']
            stud = student.objects.get(stu_id=id)
            stud.name = FullName
            stud.cgpa = cgpa
            stud.resume = file_url
            stud.mobile = number
            stud.save()
            
            messages.success(request, f'Account Details Updated ')
        return render(request, 'student/stuprofile.html',context)
    else:
        if request.method == 'POST':
            FullName = request.POST['name']
            cgpa = request.POST['cgpa']
            file = request.FILES['resume']
            fs = FileSystemStorage()
            rname = fs.save(file.name, file)
            resume = rname
            
            number =request.POST['number']
            stud = student(name=FullName,cgpa=cgpa,resume=resume,mobile=number,stu_id=id)
            stud.save()
            messages.success(request, f'Account Details Updated')
        return render(request, 'student/stuprofile.html')
    
    
def applyevent(request, id):
    events = event.objects.get(id=id)
    message = None
    if(events):
        
        context = {
        'events': events,
        }
    else:
        context = {
        'events': events,
        }
    
    if(request.method == 'POST'):
        user=request.user
        try:
            student_id = student.objects.get(stu_id = user)
            
            
        except student.DoesNotExist:
             message=messages.info(request, "Complete your profile")
        
        try:
            data = eventcon.objects.get(event_id=events,student_id=student_id)
            
            message=messages.info(request, "allready applied")
            
                
        except eventcon.DoesNotExist:
            addstudent = eventcon(event_id=events,student_id=student_id)
            addstudent.save()
            message=messages.success(request, "Applied Successfully")
    return render(request, 'student/applyevent.html',context,message)



def viewapplied(request):
    userid=request.user
    user = User.objects.get(id=userid.id)
    
    try:
        
        stuid = student.objects.get(stu_id = user)
        eventcons = eventcon.objects.filter(student_id=stuid)
        
        data = {
            'eventcons' : eventcons,
            }
    except eventcon.DoesNotExist:
        data = None
         
    if data:
        events = []
        for eventcons in eventcons:
            
            events.append(event.objects.get(id=eventcons.event_id.id))
        context = {
            'events' : events,
            }
        print(context)
    else:
        context = {
            'events' : None
            }
    
    
    return render (request, 'student/applied.html',context )

def vewresults(request):
    user = request.user
    try:
        stu = student.objects.get(stu_id=user)
    except:
        messages.info(request,"Fill Your profile info")
    
    con = eventcon.objects.filter(student_id=stu).select_related()
    
    return render (request, 'student/result.html',{ 'data':con} )