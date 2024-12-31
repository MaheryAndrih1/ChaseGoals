from django.shortcuts import render
from .models import Goal

# Create your views here.
def home(request):
    goals_list=Goal.objects.all()
    context={
        'goals_list':goals_list
    }
    return render(request, 'home.html', context)

def add_goals(request):
    return render(request, 'add_goals.html')

