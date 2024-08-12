from email import message
from django.contrib import messages
from django.shortcuts import render,redirect
from Honest.models import Registration
from django.contrib.auth import logout
from django.contrib.sessions.models import Session

# Create your views here.
def home(request):
    p1 = request.POST.get('mobile') 
    p2 = request.POST.get('password') 
    user = Registration.objects.filter(mobile=p1, password=p2)
    print(user)
    # User = request.session.get('name')
    # User = Registration.objects.all()
    if not user:
        return render(request,'Home.html',{'user':user})
    else:
        return render(request,'Loginpage.html')

def contact(request):
    p1 = request.POST.get('mobile') 
    p2 = request.POST.get('password') 
    user = Registration.objects.filter(mobile=p1, password=p2)
    print(user)
    # User = request.session.get('name')
    # User = Registration.objects.all()
    if not user:
        return render(request,'Contact.html',{'user':user})
    else:
        return render(request,'Loginpage.html')
    # return render(request,'Contact.html')

def about(request):
    return render(request,'About.html')

def registration(request):
    return render(request,'Registration.html')

def registrationlogin(request):
    if request.method == "POST":
        uname = request.POST['name']
        umobile = request.POST['mobile']
        uemail = request.POST['email']
        upassword = request.POST['password']

        ins = Registration(name=uname, mobile=umobile, email=uemail, password=upassword)
        ins.save()
        print("Data Inserted") 
    return render(request,'Loginpage.html')
    
def loginpage(request):   
    return render(request,'Loginpage.html')

def logincheck(request):
    print("here") 
    p1 = request.POST.get('mobile') 
    p2 = request.POST.get('password') 
    user = Registration.objects.filter(mobile=p1, password=p2)
    # user_type = request.GET.get('user_type') 
    print(p1) 
    print(p2)
    if not (p1 and p2): 
        return render(request, 'Loginpage.html') 
    print(user)

    # return render(request,'Home.html',{'user':user})
    # print(Registration.objects.all().filter(name='Dhruvik'))

    if not user: 
        messages.info(request,"Please enter valid Mobile and password")
        return render(request, 'Loginpage.html') 
  
    # login(request, user) 
    if user:
        # print(Registration.objects.values("name"))
        return render(request, 'Home.html',{'name':user}) 
    else:
        return render(request,'Loginpage.html',{'name':user})

    
def viewuser(request):
    User = Registration.objects.all()
    return render(request, 'Viewuser.html',{'userdata':User})

def editprofile(request, id):
    user = Registration.objects.get(id=id)
    return render(request,'edituser.html',{'user':user})

def updateprofile(request, id):
    updateid = request.POST['id']
    updatename = request.POST['name']
    updatemobile = request.POST['mobile']
    updateemail = request.POST['email']
    updatepassword = request.POST['password']

    User = Registration.objects.get(id=id)
    User.id = updateid
    User.name = updatename
    User.mobile = updatemobile
    User.email = updateemail
    User.password = updatepassword

    User.save()
    return redirect("/Viewuser")

def deleteprofile(request, id):
    us = Registration.objects.get(id=id)
    us.delete()
    return redirect("/Viewuser")

def Logout(request):
    # del request.session["name"]
    return redirect("/Logincheck")

def starter(request):
    return render(request,'starter.html')

def index(request):
    return render(request,'index.html')

def profile(request):
    return render(request,'profile.html')