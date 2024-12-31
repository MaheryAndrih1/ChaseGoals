from django.shortcuts import render
from .models import Goal
from .forms import GoalForm

# Create your views here.
def home(request):
    goals_list=Goal.objects.all()
    context={
        'goals_list':goals_list
    }
    return render(request, 'home.html', context)

def add_goals(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid:
            goal=form.save()
    else:
        form = GoalForm()
            
    return render(request, 'add_goals.html', {"form": form})

