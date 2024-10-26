from django.urls import path
from . import views

app_name = 'goals'

urlpatterns = [
    path('', views.goals_list, name='list'),
    path('new-goal/', views.goal_new, name='new-goal'),
    path('<slug:slug>', views.goal_page, name='page'),
]