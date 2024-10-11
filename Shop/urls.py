from django.urls import path
from .views import upload_Render
urlpatterns = [
    path('', upload_Render, name='upload_Render' )
]