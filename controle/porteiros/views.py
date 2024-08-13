from django.shortcuts import render

def index(request):
    return render(request, 'porteiros/index.html')  # Renderiza o template `index.html` do app `porteiros`


# Create your views here.
