from django.shortcuts import render
from django.db.models import Q
from .models import Lawyer
# Create your views here.

def search_lawyers(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')  # Get the search query from the GET parameters

        # Search for lawyers based on name, address, or practice area
        lawyers = Lawyer.objects.filter(
            
            models.Q(full_name__icontains=query) |
            models.Q(adress__icontains=query) |
            models.Q(practice_area__icontains=query)
        )

        context = {'lawyers': lawyers, 'query': query}
        return render(request, 'search_results.html', context)

    return render(request, 'search_results.html')  # You can customize the template name accordingly
