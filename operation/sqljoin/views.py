from django.shortcuts import render
from .models import Book,User


# Create your views here.

def operation_(request):
    books = Book.objects.all().prefetch_related('store_set  ')
    for book in books:
        print(book.store_set.all())
    print(books)

def operation(request):
    users = User.objects.select_related('article')

    for user in users:
        print(user)
