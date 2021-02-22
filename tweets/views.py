from django.http import HttpResponse
from django.shortcuts import render

from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse('<h1>Hello world!</h1>')

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    obj = Tweet.objects.get(id=tweet_id)
    return HttpResponse(f"<h1>Hello {tweet_id}</h1>")   
