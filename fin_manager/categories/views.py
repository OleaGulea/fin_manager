from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from fin_manager.categories.models import Category, Entry
from fin_manager.categories.forms import EntryForm


def categories_list(request):
    categories = Category.objects.all()
    return render(request, '../templates/pages/home.html', {'categories': categories})


# def book_editor(request, book_id):
#     book = Book.objects.get(pk=int(book_id))
#     return render(request, '../templates/pages/book_editor.html', {'book': book})
#
#
def entry_editor(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry_form = form.save()
            messages.success(request, "New entry was created!")
            return HttpResponseRedirect('/home/')

    else:
        form = EntryForm()

    return render(request, '../templates/pages/home.html', {'form': form})
