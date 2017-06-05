from django.shortcuts import render


from .queries import search, Error


def index(request):
    return render(request, 'search/index.html')


def results(request):
    search_query = request.GET['q']
    context = {'search_query': search_query}
    try:
        people = search(search_query)
        context['people'] = people
    except Error as e:
        context['error'] = e.message
    return render(request, 'search/index.html', context)
