from django.shortcuts import render
from .models import Main_upload, FrontImg

# Create your views here.

def main_page (request):
    apply = Main_upload.objects.filter().order_by('-title')[:4]

    context = {
        'apply' : apply,
    }

    return render (request, 'index.html', context=context)

def front_deploy (request):
    deploy = FrontImg.objects.filter().order_by('ImgName')

    context = {
        'deploy' : deploy,
    }

    return render (request, 'index.html', context=context)