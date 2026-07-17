from django.shortcuts import render , redirect , get_object_or_404
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

def studentDetails(request , id):
    student = get_object_or_404(Std , id=id)
    return render(request , 'student.html' , {"student":student})

def student_edit(request , id):
    student = get_object_or_404(Std , id=id)
    if request.method == 'POST':
        form = StdForm(request.POST ,instance=student)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
            form = StdForm(instance=student)
    return render(request , 'update.html' ,{"form":form})        

def studentDelete(request ,id ):
    student = get_object_or_404(Std , id=id)
    if request .method == 'POST':
         student.delete()
         return redirect("home")
    return render(request , 'delete.html' ,{'student':student})