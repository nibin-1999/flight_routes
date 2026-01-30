from django.shortcuts import render
from routes.models import Airport
from .forms import AirportForm, SearchForm


def add_airport(request):
    """
    Handles creation of a new Airport using AirportForm.
    Resets the form after successful submission.
    """
    form = AirportForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = AirportForm()  # Reset form after save

    return render(request, 'add_airport.html', {'form': form})


def find_path(request):
    """
    Finds all connected airports from a selected start airport
    in the chosen direction (Left or Right).
    Also determines the last reachable airport.
    """
    form = SearchForm(request.POST or None)
    path = []
    last_airport = None
    no_path = False

    if form.is_valid():
        start_airport = form.cleaned_data['airport']
        direction = form.cleaned_data['direction']

        # Check whether a connection exists in the selected direction
        next_airport = (
            start_airport.left if direction == 'L'
            else start_airport.right
        )

        if not next_airport:
            no_path = True
        else:
            current = start_airport
            visited = set()  # Prevent infinite loops in cyclic paths

            while current and current.id not in visited:
                visited.add(current.id)
                path.append(current)
                last_airport = current

                current = (
                    current.left if direction == 'L'
                    else current.right
                )

    return render(request, 'search.html', {
        'form': form,
        'path': path,
        'last_airport': last_airport,
        'no_path': no_path,
    })


def longest_duration(request):
    """
    Retrieves the airport with the maximum duration.
    """
    airport = Airport.objects.order_by('-duration').first()

    return render(request, 'duration.html', {
        'title': 'Longest Duration',
        'airport': airport
    })


def shortest_duration(request):
    """
    Retrieves the airport with the minimum duration.
    """
    airport = Airport.objects.order_by('duration').first()

    return render(request, 'duration.html', {
        'title': 'Shortest Duration',
        'airport': airport
    })
