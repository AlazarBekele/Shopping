from django.shortcuts import render
from .models import HeaderImg, News

# Create your views here.

def index (request):

    Img = HeaderImg.objects.filter()[:1]

    context = {
        'Img' : Img
    }

    return render (request,'index.html',context=context)

def Text(request):
    Text = News.objects.filter().order_by('-title')

    context = {
        'Text' : Text
    }

    return render (request, 'index.html', context=context)