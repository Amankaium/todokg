from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo


def homepage(request):
    todo_list = ToDo.objects.all()
    return render(request, "index.html", {"todo_list": todo_list})


def test(request):
    return render(request, "test.html")

def check(request):
    return HttpResponse("текшируу")


def add_todo(request):
    f = request.POST
    text = f["todo_text"]
    todo = ToDo(
        text=text
    )
    todo.save()
    return redirect(homepage)
