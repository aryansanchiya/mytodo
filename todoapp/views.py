from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render,get_object_or_404
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings

#Mail Function:
def send_text_email(subject, message, receiver_email_list):
    sender_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, sender_email, receiver_email_list)

# Create your views here.
class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def addtask(request):
    taskmodel = Task()
    if request.method == "POST":
        taskmodel.mailid = request.POST['email']
        taskmodel.name = request.POST['title']
        taskmodel.description = request.POST['description']
        taskmodel.duetime = request.POST['due_time']
        taskmodel.status = request.POST['status']
        taskmodel.save()
        return render(request,"addtask.html",{'message':"Task Added"})
    return render(request, "addtask.html")

def task(request):
    alltasks = Task.objects.all().filter(status = "pending")
    print(alltasks)
    return render(request,'task.html',{'alltasks':alltasks})

def updatetask(request,taskid):
    SingleTask = get_object_or_404(Task,id=taskid)

    #Sending Mail
    subject = "Due time is over!"
    message = f"Due time of the task {SingleTask.name} is over"
    recipient_list = [SingleTask.mailid]
    send_text_email(subject,message,recipient_list)

    if request.method == "POST": 

        SingleTask.name = request.POST['title']
        SingleTask.description = request.POST['description']
        SingleTask.duetime = request.POST['due_time']
        SingleTask.status = request.POST['status']
        SingleTask.save()
        return render(request,"task.html",{'message':"updated"})
    
    return render(request,'updatetask.html',{'SingleTask':SingleTask})

def completedtask(request):
    alltasks = Task.objects.all().filter(status = "completed")
    print(alltasks)
    return render(request,'completedtask.html',{'alltasks':alltasks})