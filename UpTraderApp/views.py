from django.shortcuts import render
from .models import MenuItem


# вывод пункта меню
def menu(request, slug):
    return render(request, 'UpTraderApp/menu.html',
                  {"slug": slug})


# вывод главной страницы
def index(request):
    queryset = MenuItem.objects.filter(parent_id=None)
    return render(request, "UpTraderApp/index.html", {"queryset": queryset})
