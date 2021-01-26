from django.shortcuts import render, HttpResponse
from .models import ToDo


def homepage(request):
    todo_list = ToDo.objects.all()
    return render(request, "index.html", {"todo_list": todo_list})


def test(request):
    return render(request, "test.html")

def check(request):
    return HttpResponse("текшируу")
