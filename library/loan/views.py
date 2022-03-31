from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
import requests

from .forms import BorrowBookForm, NewBookForm
from .models import Book

BASE_URL = 'https://covers.openlibrary.org/b/isbn/9780385533225-S.jpg'
response = requests.get(f"{BASE_URL}/")
# print(response.json())
# print(response.status_code)


def not_found_404(request, exception):
    data = { 'err': exception }
    return render(request, 'adoption/404.html', data)

def server_error_500(request):
    return render(request, 'adoption/500.html')

def index(req):
    context = { 'books': Book.objects.all() }
    return render(req, 'loan/index.html', context)

def about(req):
    return render(req, 'loan/about.html')

@login_required
def create(request):
    if request.method == 'POST':
        book = NewBookForm(request.POST)
        if book.is_valid():
            book_id = book.save().id
            return redirect("book-show", book_id=book_id)
    else:
        form = NewBookForm()
    data = {'form': form}
    return render(request, 'books/new.html', data)


@login_required
def show(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            book.borrower = request.user
            book.save()
            return redirect("book-show", book_id=book_id)
    else:
        form = BorrowBookForm(initial={'borrower': request.user})
    data = {
        'book': book,
        'form': form
    }
    return render(request, 'books/show.html', data)