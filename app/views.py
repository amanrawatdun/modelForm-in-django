from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import StdForm
from .models import Std

# Create your views here.
def home(request):
    return HttpResponse("hello world")

def stdform(request):
    if request.method == 'POST':
        std = StdForm(request.POST)
        if std.is_valid():
            std.save()
            return redirect('home')
    
    else:
        std = StdForm()
    
    return render(request ,'createForm.html' , {"std":std} )


def stdRead(request):
    
    data=Std.objects.all()

    return render(request , 'home.html',{"data":data})
        