from django.shortcuts import render

# Create your views here.
def diga_ola(request):
    return render(request, 'diga_ola.html')

