from django.urls import path
from .views import students_create , delete , print #, students_view


app_name = 'scores'

urlpatterns = [

    #path('create/', students_view, name='scores'),
    path('', students_create, name = 'scores'),
    path('delete/', delete, name = 'delete'),
    path ('print/',print,name = 'print' ),

]
