from django.shortcuts import render, redirect

from todoapp.forms import todoform
from todoapp.models import todoapp


# Create your views here.
def todofun(request):
    return render(request,"index.html")
def addtodo(request):
    form=todoform()
    if request.method=="POST":
        form=todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todofun')
    return render(request,"addtodo.html",{"form":form})
def view_todo(request):
    data=todoapp.objects.all()
    return render(request,"view_todo.html",{'data':data})
def update_todo(request,id):
    data=todoapp.objects.get(id=id)
    form=todoform(instance=data)
    if request.method=='POST':
        form=todoform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_todo')
    return render(request,'update_todo.html',{'form':form})
def del_todo(request,id):
    todoapp.objects.get(id=id).delete()
    return redirect('view_todo')