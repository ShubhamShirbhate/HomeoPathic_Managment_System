from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
# Create your views here.
def sighinuser(request):
    if request.method == 'GET':
        user = User.objects.all().count()+1
        return render(request, 'acc/sighin.html',{'form':UserCreationForm,'user':user})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                user = User.objects.all().count()
                return redirect('Create')
            except IntegrityError:
                return render(request, 'acc/sighin.html',{'form':UserCreationForm,'user':user, 'error':'Username alreaady been taken plz try anather...!'})
        else:
            user = User.objects.all().count()
            return render(request, 'acc/sighin.html',{'form':UserCreationForm,'user':user,  'error':'password need to be matched.....!'})
   


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'acc/login.html',{'form':AuthenticationForm()})
    else:
        try:
            user = authenticate(request,username= request.POST['username'], password = request.POST['password'])
            if user is None:
                return render(request, 'acc/login.html',{'form':AuthenticationForm(), 'error':'Username and password in not Valid plz try valid Username and Password'})
            else:
                login(request, user)
                return redirect('patient_view')
        except ValueError:
            return render(request, 'acc/login.html',{'form':AuthenticationForm(),'error':'fill the blank field'})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')




        