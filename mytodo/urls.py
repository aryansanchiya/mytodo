"""mytodo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from todoapp.views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
    path('addtask',views.addtask,name='addtask'),
    path('task',views.task,name='task'),
    path('updatetask/<int:taskid>',views.updatetask,name='update-task'),
    path('completedtask',views.completedtask,name='completed_task'),
]
