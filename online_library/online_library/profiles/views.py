from django.shortcuts import render, redirect

from online_library.books.models import Book
from online_library.core.profile_utils import get_profile
from online_library.profiles.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm


def profile_details(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProfileCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileEditForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            Book.objects.all().delete()
            profile.delete()
            return redirect('home page')
    else:
        form = ProfileDeleteForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'delete-profile.html', context)


