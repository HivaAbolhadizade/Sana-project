from django.shortcuts import render, redirect
from .models import Students
from django.contrib.auth.decorators import login_required
from .forms import StudentsForm

#def scores_view(request):
 #   return render(request,'scores/create_students.html', {})


@login_required(login_url='/accounts/login')
def students_create(request):
    user = request.user
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit= False)
            instance.clas = user
            instance.save()
            return redirect('scores:scores')

    form = StudentsForm()
    user = request.user
    query = Students.objects.filter(clas = user)
    #students = Students.objects.all()[0]

    return render(request, 'scores/create_students.html', {'form':form, 'students':query})


# @login_required(login_url='/accounts/login')
# def students_view(request):
#    user = request.user
#    query = Students.objects.filter(clas = user)
#    #students = Students.objects.all()[0]
#    return render(request, 'scores/scores.html', {'students':query})
