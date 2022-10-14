from django import forms
from django.forms import EmailInput, PasswordInput

from gamesplay_app.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileForm):
    class Meta:
        model = Profile
        fields = ['age', 'email', 'password']


class EditProfileForm(ProfileForm):
    pass


class DeleteProfileForm(ProfileForm):
    pass
