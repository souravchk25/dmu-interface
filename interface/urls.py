from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addTrajectory/', views.add_trajectory, name='add_trajectory'),
    path('viewTrajectories/', views.get_all_trajectories, name='view_trajectories'),
    path('download/', views.download_trajectories, name='download'),
]
