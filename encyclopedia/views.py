from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, name):
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