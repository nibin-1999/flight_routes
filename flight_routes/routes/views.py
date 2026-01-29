from django.shortcuts import render
from .forms import AirportForm


# Add a new airport view
def add_airport(request):
    form = AirportForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AirportForm()
        form = AirportForm()
    return render(request, 'add_airport.html', {'form': form})
