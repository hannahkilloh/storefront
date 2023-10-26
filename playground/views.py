from django.shortcuts import render, HttpResponse
from .models import TodoItem


def say_hello(request):
    return render(request, 'home.html')


def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})
