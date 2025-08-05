from django.shortcuts import render,redirect,HttpResponse
from votingapp.models import *
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from votingapp.models import *


# Create your views here.

def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def registration(request):
    return render(request,'registration.html')
def user_login(request):
    return render(request,'login.html')
def user_action(request):
    username=request.POST.get("username")
    data = {
       'username_exists':      Login.objects.filter(username=username).exists(),
        'error':"Username Already Exist"
    }
    if(data["username_exists"]==False):
        tbl1=Login()
        username=request.POST.get("username")
        tbl1.username=request.POST.get("username")
        password=request.POST.get("password")
        tbl1.password=password
        tbl1.Usertype="User"
        tbl1.status="Approved"
        tbl1.save()
        obj=Login.objects.get(username=username,password=password)

        u=Student_register()

        u.login_id = obj.login_id
        u.Name=request.POST.get("Name")
        u.phone_number =request.POST.get("phone")
        u.Email=request.POST.get("Email")
        u.Address=request.POST.get("Address")
        u.save()
        messages.add_message(request, messages.INFO, 'Registered successfully.')
        return redirect('registration')
    else:
        messages.add_message(request, messages.INFO, 'User name is already Exist. Sorry Registration Failed.')
        return redirect('registration')
def login_action(request):
    u=request.POST.get("username")
    p=request.POST.get("password")
    obj=authenticate(username=u,password=p)
    if obj is not None:
        if obj.is_superuser == 1:
            request.session['aname'] = u
            request.session['slogid'] = obj.id
            return redirect('admin_home')
        else:
          messages.add_message(request, messages.INFO, 'Invalid User.')
          return redirect('user_login')
    else:
        newp=p
        try:
            obj1=Login.objects.get(username=u,password=newp)

            if obj1.Usertype=="employee":
                if(obj1.status=="Approved"):
                    request.session['ename'] = u
                    request.session['slogid'] = obj1.login_id
                    return redirect('employee_home')
                elif(obj1.status=="Not Approved"):
                  messages.add_message(request, messages.INFO, 'Waiting For Approval.')
                  return redirect('user_login')
                else:
                  messages.add_message(request, messages.INFO, 'Invalid User.')
                  return redirect('user_login')
           
            elif obj1.Usertype=="User":
                if(obj1.status=="Approved"):
                    request.session['uname'] = u
                    request.session['slogid'] = obj1.login_id
                    return redirect('user_home')
                elif(obj1.status=="Not Approved"):
                  messages.add_message(request, messages.INFO, 'Waiting For Approval.')
                  return redirect('user_login')
                else:
                  messages.add_message(request, messages.INFO, 'Invalid User.')
                  return redirect('user_login')

            else:
                 messages.add_message(request, messages.INFO, 'Invalid User.')
                 return redirect('user_login')
        except Login.DoesNotExist:
         messages.add_message(request, messages.INFO, 'Invalid User.')
         return redirect('user_login')
        





def user_action(request):
   
    username=request.POST.get("username")
    data = {
       'username_exists':      Login.objects.filter(username=username).exists(),
        'error':"Username Already Exist"
    }
    if(data["username_exists"]==False):
        tbl1=Login()
        username=request.POST.get("username")
        tbl1.username=request.POST.get("username")
        password=request.POST.get("password")
        tbl1.password=password
        tbl1.Usertype="User"
        tbl1.status="Approved"
        tbl1.save()
        obj=Login.objects.get(username=username,password=password)

        u=Student_register()

        u.login = obj
        u.name=request.POST.get("Name")
        u.contact_number =request.POST.get("phone")
        u.email=request.POST.get("Email")
        u.address=request.POST.get("Address")
        u.save()
        messages.add_message(request, messages.INFO, 'Registered successfully.')
        return redirect('registration')
    else:
        messages.add_message(request, messages.INFO, 'User name is already Exist. Sorry Registration Failed.')
        return redirect('registration')
    
def admin_home(request):
    if 'aname' in request.session:
     return render(request,'master/index.html')
    else:
      return redirect('user_login')
    
def admin_logout(request):
    logout(request)
    request.session.delete()
    return redirect('user_login')


def user_home(request):
    if 'uname' in request.session:
     return render(request,'user/index.html')
    else:
      return redirect('user_login')  
    
def user_logout(request):
    logout(request)
    request.session.delete()
    return redirect('user_login')


   
def user_profile(request):
    if 'uname' in request.session:
     log_id=request.session['slogid']
     data=Student_register.objects.get(login_id=log_id)
     return render(request,'User/user_profile.html',{'data':data})
    else:
      return redirect('user_login')  
    
def profile(request):
    if 'uname' not in request.session:
        return redirect('user_login')

    if request.method == 'POST':
        try:
            obj = Student_register.objects.get(user_id=request.POST.get("user"))
            obj.name = request.POST.get("Name")
            obj.email = request.POST.get("Email")
            obj.contact_number = request.POST.get("phone_number")
            obj.address = request.POST.get("Address")
            obj.save()
            messages.success(request, 'Updated successfully..')
            return redirect('/user_profile')
        except Student_register.DoesNotExist:
            messages.error(request, 'User not found')
            return redirect('/user_profile')

    data = Student_register.objects.get(user_id=request.session['user_id'])
    return render(request, 'user/user_profile.html', {"data": data})

def batch(request):
    if 'aname' in request.session:
     data=Batch.objects.all()
     return render(request,'master/batch.html',{'data':data})
    else:
      return redirect('user_login')
    
def add_batch(request):
    if 'aname' in request.session:
       if request.method=='POST':
          obj=Batch()
          obj.batch=request.POST['batch']
          obj.save()
          return redirect('batch')
     
    else:
      return redirect('user_login')
    

def course(request):
    if 'aname' in request.session:
     data=Course.objects.all()
     return render(request,'master/course.html',{'data':data})
    else:
      return redirect('user_login')
    
def add_course(request):
    if 'aname' in request.session:
       if request.method=='POST':
          obj=Course()
          obj.course=request.POST['course']
          obj.save()
          return redirect('course')
     
    else:
      return redirect('user_login')
    
def department(request):
    if 'aname' in request.session:
     data=Department.objects.all()
     return render(request,'master/department.html',{'data':data})
    else:
      return redirect('user_login')
    
def add_department(request):
    if 'aname' in request.session:
       if request.method=='POST':
          obj=Department()
          obj.department=request.POST['department']
          obj.save()
          return redirect('department')
     
    else:
      return redirect('user_login')
    
def position(request):
    if 'aname' in request.session:
     data=Position.objects.all()
     return render(request,'master/position.html',{'data':data})
    else:
      return redirect('user_login')
    
def add_position(request):
    if 'aname' in request.session:
       if request.method=='POST':
          obj=Position()
          obj.position=request.POST['position']
          obj.save()
          return redirect('position')
     
    else:
      return redirect('user_login')
    
def notification(request):
    if 'aname' in request.session:
     data=Notification.objects.all()
     return render(request,'master/notification.html',{'data':data})
    else:
      return redirect('user_login')
    
def add_notification(request):
    if 'aname' in request.session:
       if request.method=='POST':
          obj=Notification()
          obj.status="Not Completed"
          obj.title=request.POST.get('title')
          obj.description=request.POST.get('description')
          obj.notification_date=request.POST.get('notification_date')
          obj.last_nomination_date=request.POST.get('last_nomination_date')
          obj.polling_date=request.POST.get('polling_date')
          obj.counting_date=request.POST.get('counting_date')
          obj.election_year=request.POST.get('election_year')
          obj.position=request.POST.get('position')
          obj.save()
          return redirect('notification')
     
    else:
      return redirect('user_login')
    

    
    

    

    
    
