from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add_goals/', views.add_goals, name='add goals')
]
