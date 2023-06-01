from django.shortcuts import render, redirect, get_object_or_404
from .models import Students
from django.contrib.auth.decorators import login_required
from .forms import StudentsForm, Delete

#def scores_view(request):
 #   return render(request,'scores/create_students.html', {})
list = []
@login_required(login_url='/accounts/login')
def students_create(request):
    user = request.user
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit= False)
            instance.clas = user
            if instance.name in list:
                student = Students.objects.filter(name = instance.name)
                student.delete()
            # if instance.name not in instance.list:
            #     instance.list.append(instance.name)
            # print(instance.list)
            instance.save()
            return redirect('scores:scores')

    form = StudentsForm()
    user = request.user
    query = Students.objects.filter()

    # for st in Students:
        # return render(request, 'scores/create_students.html', {'name':st.name, 'sc': st.score})

    for student in query:
        list.append(student.name)

    return render(request, 'scores/create_students.html', {'form':form, 'students':query})


# @login_required(login_url='/accounts/login')
# def students_view(request):
#    user = request.user
#    query = Students.objects.filter(clas = user)
#    #students = Students.objects.all()[0]
#    return render(request, 'scores/scores.html', {'students':query})
def delete(request):
    user = request.user
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.clas = user
            if instance.name in list:
                student = Students.objects.filter(name=instance.name)
                student.delete()
                list.remove(instance.name)

            return redirect('scores:scores')
    return redirect('scores:scores')
