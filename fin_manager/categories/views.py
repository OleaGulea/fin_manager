from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.urls.base import reverse

from fin_manager.categories.models import Category, Entry
from fin_manager.categories.forms import EntryForm, CategoryForm


def categories_list(request):
    categories = Category.objects.all()
    entries = Entry.objects.all()
    return render(request, '../templates/pages/info_manager.html', {'categories': categories, 'entries': entries})


def category_editor(request, category_id=None):
    additional_context = dict()
    if category_id is not None:
        category = Category.objects.get(pk=int(category_id))
        if request.method == 'POST':
            user = request.user
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                category_form = form.save(commit=False)
                category_form.user = user
                category_form.save()
                messages.success(request, "Category was updated!")
                return HttpResponseRedirect(reverse('info_manager'))
        else:
            additional_context['category'] = category
            form = CategoryForm(instance=category)
    else:
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
    context = {'form': form}
    context.update(additional_context)
    return render(request, '../templates/pages/new_category.html', context)


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


def delete_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()
    messages.success(request, "Category was deleted!")
    return HttpResponseRedirect(reverse('info_manager'))


def update_entry(request, entry_id):
    additional_context = dict()
    entry = Entry.objects.get(pk=int(entry_id))
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, "Entry was updated!")
            return HttpResponseRedirect(reverse('info_manager'))
    else:
        additional_context['entry'] = entry
        form = EntryForm(instance=entry)
    context = {'form': form}
    context.update(additional_context)
    return render(request, '../templates/pages/update_entry.html', context)


def delete_entry(request, entry_id):
    entry = Entry.objects.get(pk=entry_id)
    entry.delete()
    messages.success(request, "Entry was deleted!")
    return HttpResponseRedirect(reverse('info_manager'))
