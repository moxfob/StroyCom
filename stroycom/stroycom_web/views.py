from django.shortcuts import render
from .models import Services

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    services_list = Services.objects.all()
    
    categories = {}
    for service in services_list:
        if service.category not in categories:
            categories[service.category] = []
        categories[service.category].append(service)

    category_choices = Services.CATEGORY_CHOICE
    
    context = {
        'categories': categories,
        'category_choices': category_choices,
        'services_count': services_list.count(),
    }
    
    return render(request, 'services.html', context)