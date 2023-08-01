from django.shortcuts import render
from django.conf import settings

def schichtplan(request):
    context = {'MEDIA_URL': settings.MEDIA_URL}
    return render(request, 'Schichtplan.html', context)
