# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from .models import Todo

# Create your views here.

def test(request):
    return HttpResponse('Hello PyCon2017')


def index1(request):
    return render(request,'index.html')


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos,
    }
    return render(request,'index.html',context)

def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo':todo
    }
    return render(request, 'details.html', context)
