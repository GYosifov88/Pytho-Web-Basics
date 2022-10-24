from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from notes_app.core.profile_utils import get_profile
from notes_app.notes.forms import ProfileCreateForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from notes_app.notes.models import Note


def home_page(request):
    profile = get_profile()
    notes = Note.objects.all()
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
            'notes': notes,
        }

        return render(request, 'home-no-profile.html', context)

    context = {
        'notes': notes,
        'profile': profile,
    }
    return render(request, 'home-with-profile.html', context)


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


def profile_details(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    Note.objects.all().delete()
    profile.delete()
    return HttpResponseRedirect(reverse('home page'))


def add_note(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateNoteForm()

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    profile = get_profile()
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'note': note,
        'form': form,
        'profile': profile,
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        note.delete()
        return redirect('home page')
    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'note': note,
        'form': form,
    }
    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)
    profile = get_profile()
    context = {
        'note': note,
        'profile': profile
    }

    return render(request, 'note-details.html', context)
