from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoItem
# Create your views here.

def homepage(request):
    to_do_items = ToDoItem.objects.all()
    return render(request,'homepage.html',{'to_do_items':to_do_items})

def add_item_view(request):
    content = request.POST['content']
    item = ToDoItem(content = content)
    item.save()
    return HttpResponseRedirect('/homepage')
