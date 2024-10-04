from django.shortcuts import render
from .models import Obj

# Create your views here.

def index (request):
    apply = Obj.objects.all()

    context = {
        'apply' : apply
    }

    return render (request, 'index.html', context=context)