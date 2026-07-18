from django.urls import path
from .  import views

urlpatterns=[
    path('showmsg/' ,views.show_msg , name='showmsg' )
]