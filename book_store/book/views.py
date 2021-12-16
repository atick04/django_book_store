from django.shortcuts import render

from .models import Book

def index(request):
    books = Book.objects.order_by('added_date')
    context = {'books':books}
    return render(request, 'book/index.html', context)
