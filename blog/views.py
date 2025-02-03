from django.http import JsonResponse
from .models import Article

def article_list(request):
    articles = list(Article.objects.values())
    return JsonResponse(articles, safe=False, json_dumps_params={'ensure_ascii': False})

def article_detail(request, id):
    try:
        article = Article.objects.get(id=id)
        return JsonResponse(
            {"title": article.title, "text": article.text, "author": article.author},
            json_dumps_params={'ensure_ascii': False}
        )
    except Article.DoesNotExist:
        return JsonResponse({"error": "Article not found"}, status=404)