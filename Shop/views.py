from django.shortcuts import render
from .models import UploadContainer
# Create your views here.

def upload_Render (request):

    reader = UploadContainer.objects.filter().order_by('-title')[:4]

    context = {
        'reader' : reader
    }

    return render (request, 'index.html', context=context)