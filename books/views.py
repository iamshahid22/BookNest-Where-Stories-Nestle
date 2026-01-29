from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Book, Category


def home(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    books = Book.objects.all()
    categories = Category.objects.all()

    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        )

    if category_id:
        books = books.filter(category_id=category_id)

    context = {
        'books': books,
        'categories': categories,
        'selected_category': category_id
    }

    return render(request, 'books/home.html', context)


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/book_detail.html', {'book': book})
