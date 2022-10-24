from django import forms

from online_library.books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CreateBookForm(BookForm):
    pass


class EditBookForm(BookForm):
    pass

