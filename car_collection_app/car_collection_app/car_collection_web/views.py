from django.shortcuts import render, redirect

from car_collection_app.car_collection_web.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, \
    EditProfileForm, DeleteProfileForm
from car_collection_app.car_collection_web.models import Car
from car_collection_app.core.profile_utils import get_profile


def home_page(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'index.html', context)


def catalogue_page(request):
    profile = get_profile()
    cars = Car.objects.all()
    context = {
        'profile': profile,
        'cars': cars,
    }
    return render(request, 'catalogue.html', context)


def profile_create(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'profile-create.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile-delete.html', context)


def profile_details(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile-details.html', context)


def car_create(request):
    profile = get_profile()

    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')
    else:
        form = CreateCarForm()

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'car-create.html', context)


def car_edit(request, pk):
    profile = get_profile()
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')
    else:
        form = EditCarForm(instance=car)

    context = {
        'form': form,
        'profile': profile,
        'car': car,
    }

    return render(request, 'car-edit.html', context)


def car_delete(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'POST':
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue page')
    else:
        form = DeleteCarForm(instance=car)

    context = {
        'form': form,
        'car': car,
    }

    return render(request, 'car-delete.html', context)


def car_details(request, pk):
    profile = get_profile()
    car = Car.objects.get(pk=pk)
    context = {
        'car': car,
        'profile': profile
    }

    return render(request, 'car-details.html', context)



