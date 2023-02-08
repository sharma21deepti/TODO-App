from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from task.models import Task
from django.urls import reverse
from django.template import loader

# Create your views here.
def task(request):

    context={ 'success':False}
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        ins =Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context={ 'success':True}
    return render(request,'index.html',context)

def about(request):
    allTasks=Task.objects.all()
    # print(allTasks)
    # for item in allTasks:
    #     print(item.taskTitle)
    context={'tasks':allTasks}
    return render(request,'about.html',context)

def delete(request, id):
  member = Task.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('about'))

def update(request,id):
    mymember=Task.objects.get(id=id)
    template=loader.get_template('update.html')
    context={
        'allTasks':mymember,
    }
    return HttpResponse(template.render(context,request))

def updaterecord(request,id):
    title=request.POST['title']
    desc=request.POST['desc']
    member=Task.objects.get(id=id)
    member.taskTitle=title
    member.taskDesc=desc
    member.save()
    return HttpResponseRedirect(reverse('about'))
