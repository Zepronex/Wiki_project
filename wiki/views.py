from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
import os

# wiki/views.py

def home(request):
    pages = os.listdir('wiki_pages')
    pages = [page.replace('.txt', '') for page in pages if page.endswith('.txt')]
    return render(request, 'wiki/home.html', {'pages': pages})

def view_page(request, page_name):
    try:
        with open(f'wiki_pages/{page_name}.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        return redirect('edit_page', page_name=page_name)
    return render(request, 'wiki/view_page.html', {'page_name': page_name, 'content': content})


# wiki/views.py

def edit_page(request, page_name):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        os.makedirs('wiki_pages', exist_ok=True)
        with open(f'wiki_pages/{page_name}.txt', 'w') as file:
            file.write(content)
        return redirect('view_page', page_name=page_name)
    else:
        content = ''
        try:
            with open(f'wiki_pages/{page_name}.txt', 'r') as file:
                content = file.read()
        except FileNotFoundError:
            pass
        return render(request, 'wiki/edit_page.html', {'page_name': page_name, 'content': content})
