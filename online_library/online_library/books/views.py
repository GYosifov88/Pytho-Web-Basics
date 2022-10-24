from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from online_library.books.forms import CreateBookForm, EditBookForm
from online_library.books.models import Book
from online_library.core.profile_utils import get_profile
from online_library.profiles.forms import ProfileCreateForm


def home_page(request):
    profile = get_profile()
    books = Book.objects.all()
    if not profile:
        if request.method == 'POST':
            form = ProfileCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home page')
        else:
            form = ProfileCreateForm()

        context = {
            'form': form,
            'books': books,
        }

        return render(request, 'home-no-profile.html', context)

    n = 3
    books = [books[i:i + n] for i in range(0, len(books), n)]
    context = {
        'books': books,
        'profile': profile,
    }
    return render(request, 'home-with-profile.html', context)


def add_book(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateBookForm()

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditBookForm(instance=book)

    context = {
        'book': book,
        'form': form,
        'profile': profile,
    }

    return render(request, 'edit-book.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return HttpResponseRedirect(reverse('home page'))


def details_book(request, pk):
    book = Book.objects.get(pk=pk)
    profile = get_profile()
    context = {
        'book': book,
        'profile': profile
    }

    return render(request, 'book-details.html', context)


