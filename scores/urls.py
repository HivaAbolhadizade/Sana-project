from django.urls import path
from .views import students_create , delete#, students_view


app_name = 'scores'

urlpatterns = [

    #path('create/', students_view, name='scores'),
    path('', students_create, name = 'scores'),
    path ('/delete',delete,name = 'delete' )
]