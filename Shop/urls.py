from django.urls import path
from .views import Text

urlpatterns = [
     path('', Text, name='index')
]