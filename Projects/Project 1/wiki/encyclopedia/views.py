from django.shortcuts import render
from django import forms
from . import util
from django.http import HttpResponse

class wikiArticle(forms.Form):
    title = forms.CharField(label='Title: ',max_length=100)
    markdown = forms.Textarea()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def titles(request, title):
    return render(request, 'encyclopedia/titles.html', {
        "titles": util.get_entry(title.upper())
    })

def createEntries(request):
    return render(request, 'encyclopedia/entryPage.html', {
        'form': wikiArticle(),
    })