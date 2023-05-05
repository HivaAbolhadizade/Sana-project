from django.urls import path
from .views import classes_view


app_name = 'classes'

urlpatterns = [
    path('', classes_view, name='classes'),
]