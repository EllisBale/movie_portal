from django.shortcuts import render
from .models import Menu


def menu_list(request):
    """
    Shows all menu items.
    """
    menu = Menu.objects.all()
    return render(request, 'menu.html', {
        'menu': menu,
    })
