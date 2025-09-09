from django.shortcuts import render
from .models import Menu
# Create your views here.


def menu_list(request):
    """
    Shows all menu items.
    """
    menu = Menu.objects.all()
    return render(request, 'menu.html', {
        'menu': menu,
    })
        
    