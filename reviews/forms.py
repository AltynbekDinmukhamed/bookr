from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    published_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d.%m.%Y', '%m/%d/%Y']
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'published_date', 'cover_image']
