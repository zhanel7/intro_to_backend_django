from .models import Review

def review_list(request):
    reviews = list(Review.objects.values())
    return JsonResponse({'reviews': reviews})

def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return JsonResponse({'review': review})

