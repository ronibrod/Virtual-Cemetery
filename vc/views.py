from django.shortcuts import render
from django import forms
from . import models


class MyForm(forms.Form):
    task = forms.CharField(label="dy dy")


def home_page(request):
    return render(request, "vc/home_page.html", {
        "list_of_people": models.list_of_people,
        "form": MyForm()
    })


def page(request, person_name):
    return render(request, "vc/page.html", {
        "person_name": person_name
    })


def add(request):
    if request.method == "POST":
        entry = request.POST
        models.newEntry(entry)
    first_name = ""
    return render(request, "vc/add.html", {
        "first_name": first_name
    })
