from django import forms
from django.forms import EmailInput, PasswordInput

from my_music_app.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileForm):
    pass


class EditProfileForm(ProfileForm):
    pass


class DeleteProfileForm(ProfileForm):
    pass
