from django.shortcuts import render

# Create your views here.
def index(request):
    
    """ The HomePage of pizzas."""
    return render(request, 'pizzas/index.html')
