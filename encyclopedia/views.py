import secrets
from django.views.generic import UpdateView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import markdown2
from django.urls import reverse

from . import util, forms
from .models import Items
from .forms import CreateNewPage, EditPage
from django import forms

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
        return render(request, 'encyclopedia/notfound.html' )




def search(request):
    if request.method=="POST":
       q=request.POST['q']
       allitems = Items.objects.filter(title__exact=q)
       myitems = Items.objects.filter(title__contains=q)
       if allitems is not None:

           for i in util.list_entries():
               if i.upper() == q.upper():
                   page = util.get_entry(i)
                   display = markdown2.markdown(page)
                   return render(request, 'encyclopedia/entry.html', {
                       'i': q,
                       'display': display
                   })
       if len(allitems) == 0 and len(myitems)>0:


                   return render(request, 'encyclopedia/search.html', {
                     'q': q,
                     'myitems':myitems,

                   })
       else:

                   return render(request, 'encyclopedia/notfound.html')




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
               Items.objects.create(title=title,myfile=util.get_entry(title),description=content)


               return HttpResponseRedirect(reverse('entry', kwargs={'title':title}))
            else:
                return HttpResponse('<h1>SORRY, THE PAGE WITH THIS TITLE ALREADY EXIST</h1>')

    else:
        form = CreateNewPage()
        return render(request, 'encyclopedia/new.html', {
          "form":form
        })


def edit(request,title):
    item=Items.objects.get(title=title)
    form=CreateNewPage(instance=item)
    if request.method=='POST':
        form=CreateNewPage(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'encyclopedia/edit.html', {
           'form':form
        })

def random(request):
    entries=util.list_entries()
    page=secrets.choice(entries)
    return HttpResponseRedirect(reverse('entry', kwargs={'title':page}))