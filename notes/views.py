from django.shortcuts import render
from .models import Note, Topic


def home(req):
    context = {"page_name": "Notes Home"}
    notes = Note.objects.all()
    topics = Topic.objects.all()
    context |= {"notes": notes, "topics": topics}
    return render(req, "home.html", context)

def new_topic(req):
    context = {"page_name": "New Note"}
    return render(req, "new_topic.html", context)

def edit_topic(req):
    context = {"page_name": "Edit Note"}
    return render(req, "edit_topic.html", context)

def delete_topic(req):
    context = {"page_name": "Delete Note"}
    return render(req, "delete_topic.html", context)

def new_note(req):
    context = {"page_name": "New Note"}
    notes = Note.objects.all()
    topics = Topic.objects.all()
    context |= {"notes": notes, "topics": topics}
    if req.method == "POST":
        print(list(req.POST.keys()))
    return render(req, "new_note.html", context)


def edit_note(req):
    context = {"page_name": "Edit Note"}
    return render(req, "edit_note.html", context)

def delete_note(req):
    context = {"page_name": "Delete Note"}
    return render(req, "delete_note.html", context)

def search(req):
    context = {"page_name": "Search"}
    return render(req, "search.html", context)

