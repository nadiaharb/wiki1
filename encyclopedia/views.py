from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import markdown2
from django.urls import reverse

from . import util
from .models import Items
from .forms import CreateNewPage, EditPage

def index(request):


    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),

    })

def entry(request, title):
    page=util.get_entry(title)
    if page:
        display=markdown2.markdown(page)
        return render(request, 'encyclopedia/entry.html',{
            'title': title,
            'display':display,
        })
    else:
      return HttpResponse('Ooops! The page not found')




def search(request):
    if request.method=="POST":
       q=request.POST['q']
       if q in util.list_entries():
           page=util.get_entry(q)
           display = markdown2.markdown(page)
           return render(request, 'encyclopedia/entry.html', {
             'q':q,
             'display':display
           })
       else:
           myitems=Items.objects.filter(name__contains=q)


           return render(request, 'encyclopedia/search.html', {
               'q': q,
               'myitems':myitems,

           })

    else:
       return render(request, 'encyclopedia/search.html', {
        })

def create(request):
    if request.method=='POST':
        form = CreateNewPage(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['description']
            if title not in util.list_entries():
               util.save_entry(title, content)

               return HttpResponseRedirect(reverse('entry', kwargs={'title':title}))
            else:
                return HttpResponse('PAGE EXIST')

    else:
        form = CreateNewPage()
        return render(request, 'encyclopedia/new.html', {
          "form":form
        })
