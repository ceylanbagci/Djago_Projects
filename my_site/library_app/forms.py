from django import forms
from library_app.models import Book

class BookForm(forms.ModelForm):
    book_title = forms.CharField()
    book_author=forms.CharField(max_length=255)
    book_isbn_no=forms.CharField(max_length=255)
    book_pub_date=forms.DateField()

    class Meta:
        model = Book
        fields = ['book_title']
