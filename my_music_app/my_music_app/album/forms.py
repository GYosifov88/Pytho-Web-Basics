from django import forms
from django.forms import Textarea

from my_music_app.album.models import Album
from my_music_app.album.validators import genre_validator


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class CreateAlbumForm(AlbumForm):
    GENRES = (
        (0, '------'),
        (1, 'Pop Music'),
        (2, 'Jazz Music'),
        (3, 'R&B Music'),
        (4, 'Rock Music'),
        (5, 'Country Music'),
        (6, 'Dance Music'),
        (7, 'Hip Hop Music'),
        (8, 'Other')
    )

    album_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Album Name',
                'class': 'form-control',
            },
        )
    )

    artist = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Artist',
                'class': 'form-control',
            }
        )
    )

    genre = forms.ChoiceField(
        choices=GENRES,
    )

    description = forms.CharField(
        widget=Textarea(
            attrs={'placeholder': 'Description', 'class': 'form-control',}
        ),
    )

    image_url = forms.URLField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Image URL',
                'class': 'form-control',
            }
        )
    )

    price = forms.FloatField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Price',
                'class': 'form-control',
            }
        )
    )


class EditAlbumForm(AlbumForm):
    GENRES = (
        (0, '------'),
        (1, 'Pop Music'),
        (2, 'Jazz Music'),
        (3, 'R&B Music'),
        (4, 'Rock Music'),
        (5, 'Country Music'),
        (6, 'Dance Music'),
        (7, 'Hip Hop Music'),
        (8, 'Other')
    )

    album_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Album Name',
                'class': 'form-control',
            },
        )
    )

    artist = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Artist',
                'class': 'form-control',
            }
        )
    )

    genre = forms.ChoiceField(
        choices=GENRES,
    )

    description = forms.CharField(
        widget=Textarea(
            attrs={'placeholder': 'Description', 'class': 'form-control', }
        ),
    )

    image_url = forms.URLField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Image URL',
                'class': 'form-control',
            }
        )
    )

    price = forms.FloatField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Price',
                'class': 'form-control',
            }
        )
    )


class DeleteAlbumForm(AlbumForm):
    GENRES = (
        (0, '------'),
        (1, 'Pop Music'),
        (2, 'Jazz Music'),
        (3, 'R&B Music'),
        (4, 'Rock Music'),
        (5, 'Country Music'),
        (6, 'Dance Music'),
        (7, 'Hip Hop Music'),
        (8, 'Other')
    )

    album_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Album Name',
                'class': 'form-control',
            },
        )
    )

    artist = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Artist',
                'class': 'form-control',
            }
        )
    )

    genre = forms.ChoiceField(
        choices=GENRES,
    )

    description = forms.CharField(
        widget=Textarea(
            attrs={'placeholder': 'Description', 'class': 'form-control', }
        ),
    )

    image_url = forms.URLField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Image URL',
                'class': 'form-control',
            }
        )
    )

    price = forms.FloatField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Price',
                'class': 'form-control',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'