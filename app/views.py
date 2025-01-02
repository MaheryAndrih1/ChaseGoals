from django.shortcuts import render, redirect
from .models import Goal
from .forms import GoalForm

# Create your views here.
def home(request):
    goals_list=Goal.objects.all()
    context={
        'goals_list':goals_list
    }
    return render(request, 'home.html', context)

def add_goal(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid:
            goal=form.save()
    else:
        form = GoalForm()
            
    return render(request, 'add goal.html', {"form": form})

def delete_goal(request, goal_id):
    goal = Goal.objects.get(pk = goal_id)
    goal.delete()
    return redirect('home')

def achieved_goal(request, goal_id):
    goal = Goal.objects.get(pk = goal_id)
    goal.is_achieved = not goal.is_achieved
    goal.save()
    return redirect('home')

def update_goal(request, goal_id):
    goal = Goal.objects.get(pk = goal_id)
    print('Update called')
    return redirect('home')