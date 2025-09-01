from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Film
from .forms import FilmForm

# Create your views here.

def film_list(request):
    films = Film.objects.filter(is_coming_soon=False)
    hero_films = Film.objects.filter(is_hero_image=True)
    return render(request, 'films.html', {
        'films': films,
        'hero_films': hero_films,
        
        })

def film_detail(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    return render(request, 'films_detail.html', {'film': film})



# Admin/staff

# Film CRUD

@staff_member_required
def manage_films(request):
    films = Film.objects.all().order_by("title")
    return render(request, "manage_films.html", {"films": films})


@staff_member_required
def film_create(request):
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('films')
    else:
        form = FilmForm()
    return render(request, 'film_form.html', {'form': form})


@staff_member_required
def film_update(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect("films")
    else:
        form = FilmForm(instance=film)
    return render(request, 'film_form.html', {'form': form})


@staff_member_required
def film_delete(request, pk):
    film = get_object_or_404(Film, pk=pk)
    film.delete()
    return redirect('manage_films')
    