from django.urls import path
from . import views

urlpatterns=[
    path('home/' ,views.stdRead , name='home'),
    path('create/form/', views.stdform, name='create_form'),
    path('studentdetails/<int:id>', views.studentDetails, name='studentdetails'),
    path('studentedit/<int:id>', views.student_edit, name='studentedit'),
    path('studentdelete/<int:id>', views.studentDelete, name='studentDelete'),

]