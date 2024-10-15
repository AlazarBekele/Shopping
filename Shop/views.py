from django.shortcuts import render
from .models import UploadContainer, SecondImg
# Create your views here.

def upload_Render (request):

    reader = UploadContainer.objects.filter().order_by('-title')[:4]
    BackImg = SecondImg.objects.filter().order_by('-title')[:2]

    context = {
        'reader' : reader,
        'BackImg' : BackImg,
    }

    return render (request, 'index.html', context=context)