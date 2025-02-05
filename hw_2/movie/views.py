from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    movies = list(Movie.objects.values())
    return JsonResponse(movies, safe=False, json_dumps_params={'ensure_ascii': False})

def movie_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
        return JsonResponse(
            {"title": movie.title, "description": movie.description, "director": movie.director},
            json_dumps_params={'ensure_ascii': False}
        )
    except Movie.DoesNotExist:
        return JsonResponse({"error": "Movie not found"}, status=404)

def movie_list_page(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movies': movies})
