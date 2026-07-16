from django.urls import path
from . import views

urlpatterns=[
    path('home/' ,views.stdRead , name='home'),
    path('create/form/', views.stdform, name='create_form'),
]