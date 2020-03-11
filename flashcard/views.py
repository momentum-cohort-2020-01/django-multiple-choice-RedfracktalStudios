from django.shortcuts import render
from django.views.decorators.http import require_GET

def registeruser(request):
  return render(request, 'flashcard/registeruser.html')
