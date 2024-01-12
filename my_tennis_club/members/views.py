from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForms
from .models import Todo


def login(request):
    if request.method == "POST":
        form = TodoForms(request.POST)
        if form.is_valid():
            form.save()
    form = TodoForms()

    page = {
        "forms": form
    }
    return render(request, "todo.html", page)