

from django.shortcuts import render
import markdown2
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def md_to_html(title):
    page = util.get_entry(title)
    markdowner = markdown2.Markdown()
    if page == None:
        return None
    else:
        return markdowner.convert(page)

def entry(request, title):
    content_html = md_to_html(title)
    if content_html == None:
        return render(request, "encyclopedia/error.html",{
            "message":"This page does not exist"
        })
    return render(request, "encyclopedia/entry.html", {
        "title" : title,
        "content": content_html
    })

def search(request):
    if request.method == "POST":
        item_searched = request.POST['q']
        content_html = md_to_html(item_searched)
        if content_html != None:
            return entry(request, item_searched)
        else:
            all_entries = util.list_entries()
            elements = []
            for item in all_entries:
                if item_searched.lower() in item.lower():
                    elements.append(item)
            return render(request, "encyclopedia/search.html",{
                "list":elements
            })
def random_page(request):
    rand_choice= random.choice(util.list_entries())
    return entry(request, rand_choice)

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    elif request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        exists = util.get_entry(title)
        if exists is not None:
            return render(request, "encyclopedia/error.html",{
            "message":"This page already exists"
        })
        else:
            util.save_entry(title, content)
            return entry(request, title)  


def edit(request):
    if request.method == 'POST':
        input_title = request.POST['title']
        text = util.get_entry(input_title)
        return render(request, "encyclopedia/edit.html", {
            "content": text,
            "title": input_title
        })

def save_edit(request):
    title = request.POST['title']
    content = request.POST['content']
    util.save_entry(title, content)
    return entry(request, title)