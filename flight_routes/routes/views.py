from django.shortcuts import render

from routes.models import Airport
from .forms import AirportForm, SearchForm


# Add a new airport view
def add_airport(request):
    form = AirportForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AirportForm()
        form = AirportForm()
    return render(request, 'add_airport.html', {'form': form})


# Find path view
def find_path(request):
    path = []
    form = SearchForm(request.POST or None)

    if form.is_valid():
        airport = form.cleaned_data['airport']
        direction = form.cleaned_data['direction']

        current = airport
        visited = set()

        while current and current.id not in visited:
            visited.add(current.id)
            path.append(current)
            current = current.left if direction == 'L' else current.right

    return render(request, 'search.html', {
        'form': form,
        'path': path,
    })


# Find airport with the longest duration
def longest_duration(request):
    airport = Airport.objects.order_by('-duration').first()
    return render(request, 'duration.html', {
        'title': 'Longest Duration',
        'airport': airport
    })
