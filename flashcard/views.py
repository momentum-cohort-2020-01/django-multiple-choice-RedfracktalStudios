from django.shortcuts import render


def home(request):
    return render(request, 'flashcard/base.html')


def one(request):
    return render(request, 'flashcard/one.html')


def two(request):
    return render(request, 'flashcard/two.html')


def three(request):
    return render(request, 'flashcard/three.html')
