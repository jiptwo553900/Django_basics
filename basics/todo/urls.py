from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:pk>/update', views.TaskUpdateView.as_view(), name='todo_update'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='todo_delete'),

]