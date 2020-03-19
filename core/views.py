from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    context = {}
    return render(request, 'home.html', context)


def flashcards(request):
    context = {}
    return render(request, 'core/flashcards.html', context)
