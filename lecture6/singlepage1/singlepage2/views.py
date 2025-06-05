from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.urls import path

# Create your views here.
def index(request):
    return render(request, 'singlepage2/index.html')

texts = [1, 2, 3]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        return Http404('No such section')