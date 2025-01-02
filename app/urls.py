from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add_goal/', views.add_goal, name='add goal'),
    path('delete_goal/<int:goal_id>/', views.delete_goal, name='delete goal'),
    path('update_goal/<int:goal_id>/',views.update_goal, name='update goal'),
    path('achieved_goal/<int:goal_id>/', views.achieved_goal, name="achieved goal" ),
]
