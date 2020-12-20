from django import forms
from django.shortcuts import render

from . import util

# create our form class
class SearchInputForm(forms.Form):
    input_field = forms.CharField(label='search')

class NewpageInputForm(forms.Form):
    title_field = forms.CharField(label="Title")

def index(request):
    if request.method == "POST":
        form = SearchInputForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["input_field"]
            return wiki(request, search)
        else:
            return render(request, "encyclopedia/index.html",{
                "form":form
            })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form":SearchInputForm()
    })

def wiki(request, name):
    """ Returns a search about a word """
    if util.get_entry(name):
        return render(request, "encyclopedia/entry.html", {
            "name":util.get_entry(name),
            "title":name
        })
    else:
        error = "PAGE NOT FOUND"
        error_code = "404"
        return render(request, "encyclopedia/errors.html", {
            "error":error,
            "error_code":error_code
        })

def newPageEntry(request):
    return render(request, "encyclopedia/createpage.html", {
        "newpageform":NewpageInputForm()
    })
