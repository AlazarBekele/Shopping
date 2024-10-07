from django.shortcuts import render
from .models import Main_upload

# Create your views here.

def main_page (request):
    
    apply = Main_upload.objects.filter().order_by('-title')[:4]
    front_Image = Main_upload.objects.filter().order_by('title')

    context = {
        'apply' : apply,
        'front_Image' : front_Image
    }

    return render (request, 'index.html', context=context)