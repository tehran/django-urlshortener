from django.shortcuts import render, get_object_or_404, redirect
from .models import ShortenedURL
from .forms import ShortenURLForm
from django.urls import reverse

def shorten_url(request):
    if request.method == "POST":
        form = ShortenURLForm(request.POST)
        if form.is_valid():
            shortened_url = form.save()
            base_url = request.build_absolute_uri('/')  # Get the base URL
            return redirect(reverse('result', args=[shortened_url.pk]) + f"?base_url={base_url}")  # Pass the base URL as a query parameter
    else:
        form = ShortenURLForm()
    return render(request, 'shortener/index.html', {'form': form})

def result(request, pk):
    shortened_url = get_object_or_404(ShortenedURL, pk=pk)
    base_url = request.GET.get('base_url', '')  # Get the base URL from the query parameters
    return render(request, 'shortener/result.html', {'shortened_url': shortened_url, 'base_url': base_url})

def redirect_url(request, short_code):
    shortened_url = get_object_or_404(ShortenedURL, short_code=short_code)
    return redirect(shortened_url.original_url)