from django.shortcuts import render

# Create your views here.
def scores_view(request):
    return render(request,'scores/scores.html', {})
