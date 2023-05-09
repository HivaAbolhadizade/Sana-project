from django.urls import path
from .views import scores_view


app_name = 'scores'

urlpatterns = [
    path('', scores_view, name='classes'),
]