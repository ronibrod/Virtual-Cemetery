from django.db import models

from . import views


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=12)


list_of_people = ["דוד בן גוריון", "משה שרת", "גולדה מאיר", "לוי אשכול", "יצחק רבין"]


class Entry(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, default="")
    date_of_birth = models.DateField(default="2000-01-01")
    date_of_death = models.DateField(default="2000-01-01")
    body = models.CharField(max_length=2000)
    image = models.ImageField()


def newEntry(entry):
    a = {}
    a['first_name'] = entry['first_name']
    a['last_name'] = entry['last_name']
    a['date_of_birth'] = entry['date_of_birth']
    a['date_of_death'] = entry['date_of_death']
    a['body'] = entry['body']
    a['image'] = entry['image']
    Entry.save(Entry(**a))


class ListOfEntries(models.Model):
    entry = list_of_people
