from django.shortcuts import render, redirect
from .models import Goal
from django.contrib.auth.decorators import login_required
from . import forms
#from django.http import HttpResponse

# Create your views here.
def goals_list(request):
    goals = Goal.objects.all().order_by('-created_date') # This will get all the goals from the database and order them by the created_date field in descending order
    return render(request, 'goals/goals_list.html', {'goals': goals})

def goal_page(request, slug):
    goal = Goal.objects.get(slug=slug) # This will get all the goals from the database and order them by the created_date field in descending order
    return render(request, 'goals/goal_page.html', {'goal': goal})

@login_required(login_url='/users/login/')
def goal_new(request):
    if request.method == 'POST':
        form = forms.CreateGoalForm(request.POST, request.FILES)
        if form.is_valid():
            # save goal to db
            newgoal = form.save(commit=False)
            newgoal.owner = request.user
            newgoal.save()
            return redirect('goals:list')
    else:
        form = forms.CreateGoalForm()
    return render(request, 'goals/goal_new.html', {'form': form})
