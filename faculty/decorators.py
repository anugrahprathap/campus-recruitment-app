from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group

def unauth_user(viewfun):
    def wrapper_fun(request,*args, **kwargs):
        if (request.user.is_authenticated):
            
            a=Group.objects.all()
            print(a)
            type = request.user.groups.all()
            print(type)
            if type is not None:
                if(type[0] == a[0]):
                    return redirect('crshome')
                if(type[0] == a[1]):
                    
                    return redirect('cmphome')
                if(type[0] == a[2]):
                    return redirect('pcoHome')
                if(type[0] == a[4]):
                    return redirect('stu_home')
                if(type[0] == a[3]):
                    return HttpResponse("Yoy are not authorised")
                
        else:
            
            return viewfun(request, *args, **kwargs)
    
    return wrapper_fun
        
def allowed_users(allowed_roles=[]):
    def decorators(viewfun):
        def wrapper_fun(request,*args, **kwargs):
            group =None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                
            if group in allowed_roles:   
                return viewfun(request, *args, **kwargs)
            else:
                return HttpResponse(request,"You are not authorised")
        return wrapper_fun
    return decorators



