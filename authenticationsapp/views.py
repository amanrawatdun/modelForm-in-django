from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
# Create your views here.
def register_view(request):
    if request.method  == 'POST':
       form=RegistrationForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request , "Resgitration success")
           return redirect('login')
       else:
           messages.error(request , "Registration failed , Please correct the errors belows ")
    else:
        form=RegistrationForm()
    return render(request , 'accounts/register.html',{"form":form})


def login_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)
        print(user)
        if user is not None:
            login(request , user)
            messages.success(request , "login successfully")
            return redirect('dashboard')
        else:
            messages.error(request , "something wrong! check your cardentails")
    return render(request , 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request , "logout succesfully")
    return redirect('login')


@login_required(login_url='login')
def dashboard_view(request):
    return render(request , 'accounts/dashboard.html')
