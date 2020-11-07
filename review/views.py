from django.shortcuts import render

# Create your views here.
def review_list(request):
    return render(request, "../templates/review/review_list.html")