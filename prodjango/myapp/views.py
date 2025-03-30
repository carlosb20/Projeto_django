from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Orcamento



def index(request):
    print(request.POST.get('peca'))
    if request.method == 'POST':
        pec = request.POST.get('peca')
        prec = request.POST.get('preco')
        #Orcamento.objects.create(peca=pec,preco=prec)


        #if Orcamento.objects.filter(peca=peca).exists():
            
            #pass
        #else:
        # Cria um novo registro se o nome for único
            #Orcamento.objects.create(peca=peca,preco=preco)
            
    context = Orcamento.objects.all()
    itens = {'pecacarro':context}

    return render(request,'myapp/index.html',itens)
    


def contato(request):

    obj = Orcamento.objects.all()

    text = {'peca':obj}
    
    return render(request,'myapp/contato.html',text)
    