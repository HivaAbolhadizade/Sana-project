from django.shortcuts import render

# Create your views here.
def classes_view(request):
    return render(request,'classes/classes.html', {})
