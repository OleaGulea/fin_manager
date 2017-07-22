from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls.base import reverse

from fin_manager.categories.models import Category, Entry
from fin_manager.categories.forms import EntryForm, CategoryForm


# def categories_list(request):
#     categories = Category.objects.all()
#     return render(request, '../templates/pages/home.html', {'categories': categories})


def new_category(request):
    if request.method == 'POST':
        user = request.user
        form = CategoryForm(request.POST)
        if form.is_valid():
            category_form = form.save(commit=False)
            category_form.user = user
            category_form.save()
            messages.success(request, "New category was created!")
            return HttpResponseRedirect(reverse('home'))

    else:
        form = CategoryForm()
    return render(request, '../templates/pages/new_category.html', {'form': form})


def entry_editor(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New entry was created!")
            return HttpResponseRedirect(reverse('home'))

    else:
        form = EntryForm()

    return render(request, '../templates/pages/home.html', {'form': form})
