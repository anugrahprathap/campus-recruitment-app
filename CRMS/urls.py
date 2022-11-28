"""CRMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from company import views as comp_views
from django.contrib.auth import views as auth_views
from faculty import views as home_views
from student import views as student_view
from django.conf import settings #add this
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
     path('admin/', admin.site.urls),
     path('',include('faculty.urls')),
     path('login/',home_views.login_page,name="complogin"),
     path('logout/',home_views.logout_user,name="logout"),
     path('compregister/',comp_views.register,name='compregister'),
     path('comstats/',comp_views.comstats,name='comstats'),
     path('cmphome/',comp_views.CmpHome,name='cmphome'),
     path('stu_reg/',student_view.stu_register,name='stu_register'),
     path('pcostats/',home_views.pcostats,name='pcostats'),
     path('adminstats/',home_views.adminstats,name='adminstats'),
     path('stu_home/',student_view.stu_home,name='stu_home'),
     path('crs_home/',home_views.admin_home,name='crshome'),
     path('addPco/',home_views.addPco,name='addPco'),
     path('viewPco/',home_views.viewPco,name='viewPco'),
     path('pcohome/',home_views.pco,name="pcoHome"), 
     path('addEvent/',home_views.addEvent,name='addevent'),
     path('viewEvent/',home_views.viewEvent,name='viewEvent'),
     path('Stuview/',student_view.Stuview,name='Stuview'),
     path('stuprof/',student_view.stuProfile,name='stuprof'),
     path('apply/<int:id>',student_view.applyevent,name="apply"),
     path('viewapplied/',student_view.viewapplied,name="applied"),
     path('viewStudent/',home_views.viewStudent,name='viewStudent'),
     path('viewStudentcom/',comp_views.viewStudentcom,name='viewStudentcom'),
     path('pendingCom/',comp_views.pendingCom,name='pendingCom'),
     path('approveCom/',home_views.approveCom,name='approveCom'),
     path('addplaced/',home_views.addplaced,name='addplaced'),
     path('vewresults/',student_view.vewresults,name='vewresults'),
     path('placedstu/',home_views.placedstu,name='placedstu'),
     path('viwecom/',home_views.viwecom,name='viwecom'),
     path('viewPcocom/',comp_views.viewPcocom,name='viewPcocom'),
     path('searchstu/<int:id>',csrf_exempt(home_views.searchstu),name='searchstu'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
