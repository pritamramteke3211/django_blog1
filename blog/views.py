from django.shortcuts import render, HttpResponse

# Create your views here.
def bhome(request):
    return HttpResponse('<h1>It\'s Working</h1>')

