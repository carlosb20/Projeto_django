from django.shortcuts import render
from django.http import HttpResponse
from .models import Orcamento

def index(request):

    pec = request.POST.get('peca')
    pre = request.POST.get('preco')
    print(dir(request))

    print(pec)
    print(pre)

    #items = Orcamento.objects.all()
    #text = {'val': items}
    
    return render(request,'myapp/index.html')


def contato(request):
    
    return render(request,'myapp/contato.html')
    