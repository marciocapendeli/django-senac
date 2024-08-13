from django.shortcuts import render
def index(request):
    return render(request, 'usuarios/index.html')  # Renderiza o template `index.html` do app `usuarios`


# Create your views here.
