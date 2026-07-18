from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def show_msg(request):
    messages.info(request , "this is info msg")
    messages.success(request , "this is success")
    messages.warning(request , "this is warning")
    messages.error(request , "Action failed /error")
    return render(request , 'showmsg.html')
    
