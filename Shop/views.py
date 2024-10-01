from django.shortcuts import render
from .models import News

# Create your views here.


def Text(request):
    Text = News.objects.filter().order_by('-title')
    imagepost = News.objects.all()
    
    context = {
        'Text' : Text,
        'imagepost' : imagepost
    }

    return render (request, 'index.html', context=context)