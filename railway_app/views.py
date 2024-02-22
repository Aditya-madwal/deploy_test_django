from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import railmodel

# Create your views here.

def homeview(request) :
    if request.method =='POST' :
        name = request.POST['name']
        age = request.POST['age']
        new_object = railmodel.objects.create(name = name, age = age)
        new_object.save()

        return redirect(homeview)
    return render(request, 'home.html', {})

