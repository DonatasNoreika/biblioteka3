from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    # Suskaičiuokime keletą pagrindinių objektų
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Laisvos knygos (tos, kurios turi statusą 'g')
    num_instances_available = BookInstance.objects.filter(status__exact='g').count()

    # Kiek yra autorių
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)


def authors(request):
    paginator = Paginator(Author.objects.all(), 1)
    page_number = request.GET.get('page')
    paged_authors = paginator.get_page(page_number)
    context = {
        'authors': paged_authors
    }
    return render(request, 'authors.html', context=context)


def author(request, author_id):
    single_author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author.html', {'author': single_author})


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 5


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


def search(request):
    """
    paprasta paieška. query ima informaciją iš paieškos laukelio,
    search_results prafiltruoja pagal įvestą tekstą knygų pavadinimus ir aprašymus.
    Icontains nuo contains skiriasi tuo, kad icontains ignoruoja ar raidės
    didžiosios/mažosios.
    """
    query = request.GET.get('query')
    search_results = Book.objects.filter(Q(title__icontains=query) | Q(summary__icontains=query))
    return render(request, 'search.html', {'books': search_results, 'query': query})