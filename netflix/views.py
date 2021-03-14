from django.shortcuts import render, redirect
from . forms import movieForm
from . models import movies
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required
def index(request):
    movie = movies.objects.all()
    return render(request, "index.html", {
        'movie': movie
    })

@login_required
def create(request):
    form = movieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "create.html", {
        'form': form
    })


@login_required
@permission_required("netflix.view_movie")
def show(request, id):
    movie = movies.objects.get(pk=id)
    return render(request, "show.html", {
        'movie': movie
    })


@login_required
def update(request, id):
    movie = movies.objects.get(pk=id)
    form = movieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "update.html", {
        'form': form,
        'movie': movie
    })


@login_required
def delete(request, id):
    movie = movies.objects.get(pk=id)
    movie.delete()
    return redirect("index")