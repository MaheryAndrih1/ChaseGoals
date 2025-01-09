from django.shortcuts import render, redirect
from .models import Goal
from .forms import GoalForm
from django.http import JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
@ensure_csrf_cookie
def home(request):
    goals_list = Goal.objects.all()
    goals_data = [{
        'id_goal': goal.id_goal,
        'name_goal': goal.name_goal,
        'is_achieved': goal.is_achieved,
        'date_created': goal.date_created.strftime('%Y-%m-%d %H:%M:%S')
    } for goal in goals_list]
    
    context = {
        'goals_list': json.dumps(goals_data)
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

@ensure_csrf_cookie
def update_goal(request, goal_id):
    if request.method == "POST":
        goal = Goal.objects.get(pk=goal_id)
        data = json.loads(request.body)
        goal.name_goal = data.get('name_goal')
        goal.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

def get_goals(request):
    goals = Goal.objects.all()
    goals_data = [{'id_goal': goal.id_goal, 
                   'name_goal': goal.name_goal,
                   'is_achieved': goal.is_achieved,
                   'date_created': goal.date_created} for goal in goals]
    return JsonResponse(goals_data, safe=False)