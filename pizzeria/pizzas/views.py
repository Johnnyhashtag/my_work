from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    
    """ The HomePage of pizzas."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    # Show all pizzas.
    pizzas = Pizza.objects.order_by('id')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)