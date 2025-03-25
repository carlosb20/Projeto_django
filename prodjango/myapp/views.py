from django.shortcuts import render
from .models import Orcamento

def index(request):

    items = Orcamento.objects.all()

    text = {'val': items}
    
    return render(request,'myapp/index.html' , text)


def contato(request):
    return render(request,'myapp/contato.html')