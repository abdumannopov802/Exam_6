from django.shortcuts import render
from .models import *

# Create your views here.

def contentView(request):
    contents = ContentManager.objects.all()
    return render(request, 'index.html', {'contents':contents})