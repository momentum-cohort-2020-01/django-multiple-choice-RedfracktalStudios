from django.shortcuts import render
from .models import Deck


def home(request):

    context = {}
    return render(request, 'home.html', context)


def flashcards(request):
    qs = Deck.objects.all()
    context = {'decks': qs}
    return render(request, 'core/flashcards.html', context)
