from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from student.forms import UserRegForm
from .models import company
from django.contrib.auth.models import User
from faculty.decorators import allowed_users
from django.contrib.auth.models import Group
from faculty.models import event
from student.models import student,eventcon
from django.contrib.auth.hashers import make_password
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from .tockens import account_activation_token  
from django.core.mail import EmailMessage
from django.template.loader import render_to_string  
from .form import regform
from faculty.models import event,pcoAdd

def register(request):
    new_var = request.POST or None
    form = regform(new_var)
    
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get("name")
            mail = form.cleaned_data.get("email")
            passw = make_password(form.cleaned_data.get("Password"))
            comp_name = form.cleaned_data.get("comp_name")
            location = form.cleaned_data.get("location")
            description = form.cleaned_data.get("description")
            Phone = form.cleaned_data.get("Phone")
            url = form.cleaned_data.get("email")
            linkedin = form.cleaned_data.get("linkedin")
            if User.objects.filter(username=mail).count():
                messages.error(request, f'Account details allready exists')
            else:
                user = User(username=mail,password=passw)
                user.save()
                id = User.objects.get(username=mail)
                comp = company(name=name,comp_name=comp_name,location=location,description=description,mobile=Phone,mail=mail,url=url,linkedin=linkedin,login_id=id)
                comp.save()
                g = Group.objects.get(name='pending')
                users = User.objects.get(username=mail)
                g.user_set.add(users)
                messages.success(request, f'Account Details Added ')
            return redirect('my-home')
            #***********************
            # current_site = get_current_site(request)  
            # mail_subject = 'Activation link has been sent to your email id'  
            # message = render_to_string('acc_active_email.html', {  
            #     'user': user,  
            #     'domain': current_site.domain,  
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
            #     'token':account_activation_token.make_token(user),  
            # })  
            # to_email = mail 
            # email = EmailMessage(
            #             mail_subject, message, to=[to_email]  
            # )  
            # email.send()         
    return render(request, 'company/register.html',{ 'form':form})
@login_required
@allowed_users(allowed_roles=['comp'])
def CmpHome(request):
    return render(request, 'company/cmphome.html')


def viewStudentcom(request):
    user = company.objects.get(login_id = request.user)
    events = event.objects.filter(comp=user)
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
        
        
        return render(request, 'company/viewstu.html',context)
        
    
    # eventcons = eventcon.objects.filter(student_id=stuid)
    return render(request, 'company/viewstu.html',value )

@login_required
@allowed_users(allowed_roles=['pending'])
def pendingCom(request):
    return render(request, 'company/pending.html')
@login_required
@allowed_users(allowed_roles=['comp'])
def comstats(request):
    return render(request, 'company/stats.html')

@login_required
@allowed_users(allowed_roles=['comp'])

def viewPcocom(request):
    
    pco = User.objects.filter(groups__name='pco')
    pco = pcoAdd.objects.all()
    context = {
    'pco': pco,
    }
    print(pco)
    print(context)
    return render(request, 'company/viewPcocom.html',context )