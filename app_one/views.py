from django.http import request
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import Show, ShowManager
from time import strftime, strptime

def shows(request):
    context = {
        'all_shows': Show.objects.all(),
    }
    return render(request, "shows.html", context)

def new(request):
    return render(request, 'shows_new.html')

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:
        show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            description = request.POST['description'])
        show.save()
    return redirect('/')

def edit(request, id):
    context = {
        'show': Show.objects.get(id=id),
    }
    return render(request, 'shows_edit.html', context)

def edit_show(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{id}/edit")
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST["title"]
        show.network = request.POST["network"]
        show.release_date = request.POST["release_date"]
        show.description = request.POST["description"]
        show.save()
    return redirect(f'/info/{id}')

def info(request, id):
    context = {
        'show': Show.objects.get(id=id),
    }
    return render(request, 'show_info.html', context)

def delete(request, id):
    tv_show = Show.objects.get(id=id)
    tv_show.delete()
    return redirect('/')