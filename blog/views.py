from django.shortcuts import render, get_object_or_404
from blog.forms import *
from blog.models import *

def meetings(request):
    return render(request,"meetings.html",context={})

def meeting_details(request):
    return render(request,"meeting_details.html",context={})


def index(request):
    form = EmailForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()

    contact = leksiya.objects.all()
    name = Rasmlar.objects.all()
    context = {
        "name": name,
        "contact": contact,
        "form": form,
    }
    return render(request, "index.html", context=context)



def index_detel(request, id):
    cofe = get_object_or_404(Rasmlar,id=id)
    context = {
        "cofe": cofe,
    }
    return render(request, 'detel.html', context=context)

def index_detel2(request, id):
    contact = get_object_or_404(Rasmlar,id=id)
    context = {
        "contact": contact,
    }
    return render(request, 'detel2.html', context=context)