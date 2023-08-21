from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime as dt
from books.models import Book


def home_view(request):
    return redirect(reverse('books'))


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def page_by_pub_date(request, pub_date):
    pub_date = dt.strptime(pub_date, '%d.%m.%Y').date()
    books = Book.objects.filter(pub_date=pub_date).order_by('pub_date')
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    previous_pub_date = None
    next_pub_date = None

    previous_book = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    next_book = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()

    if previous_book:
        previous_pub_date = previous_book.pub_date
    if next_book:
        next_pub_date = next_book.pub_date

    context = {
        'books': page,
        'pub_date': pub_date,
        'previous_pub_date': previous_pub_date,
        'next_pub_date': next_pub_date,
    }
    return render(request, 'books/books_list.html', context)
