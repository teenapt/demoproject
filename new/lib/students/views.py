from django.shortcuts import render,redirect
from students.models import CustomUser
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        fname=request.POST['f']
        lname=request.POST['l']
        e=request.POST['e']
        pl=request.POST['pl']
        n=request.POST['n']

        if(p==cp):
            user=CustomUser.objects.create_user(username=u,password=p,first_name=fname,last_name=lname,email=e,place=pl,phone=n)
            user.save()
            return redirect('books:home')
        else:
            return HttpResponse("passwords are not match")
    return render(request,'register.html')

@login_required
def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p= request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('books:home')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)
    return redirect('students:login')
