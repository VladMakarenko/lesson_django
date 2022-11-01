import random
from random import randint

from django.http import HttpResponse
from django.shortcuts import render


def even_odd(request):
    return render(request, 'odd_even/even_odd.html')


def index(request):
    return render(request, 'main/first.html')


def first(request):
    random_num = randint(1, 20)
    list_letters = 'qwertyuiopasdfghjklzxcvbnm'
    length_slug = randint(5, 10)
    random_slug = "".join(random.sample(list_letters, length_slug))
    return render(request, 'main/index.html', {'random_num': random_num, 'random_slug': random_slug})


def random_id(request, id):
    return render(request, 'main/random_id.html', {'id': id})


def r_slug(request, slug):
    return render(request, 'main/random_slug.html', {'slug': slug})


def articles(request):
    return HttpResponse("articles")


def archive(request):
    return HttpResponse("<h1>archive</h1>")


def users(request, user_number=''):
    if user_number:
        return HttpResponse(f'user_number={user_number}')
    else:
        return HttpResponse('users')


def article(request, article_number='', slug_text=''):

    if slug_text:
        return render(request, 'odd_even/slug.html', {"slug_text": slug_text})
    elif article_number:
        return render(request, 'odd_even/even_odd.html', {"article_number": article_number})
    else:
        return HttpResponse('article')


def regular(request):
    return HttpResponse('regular')
