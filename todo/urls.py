from django.urls import path
from . import views


urlpatterns = [
    path('find-all', views.findAll),
    path('create', views.createTask),
    path('find/<int:id>', views.findTaskById),
    path('update/<int:id>', views.updateTask),
    path('delete/<int:id>', views.deleteTask),
]
