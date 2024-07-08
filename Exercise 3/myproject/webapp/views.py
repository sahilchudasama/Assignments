from django.shortcuts import render
from datetime import datetime

def index(request):
    current_datetime = datetime.now()
    context = {
        'current_datetime': current_datetime,
    }
    return render(request, 'index.html', context)
