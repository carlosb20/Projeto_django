from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Orcamento


@csrf_exempt
def index(request):

    if request.method == 'POST':
        pec = request.POST.get('peca')
        prec = request.POST.get('preco')
        #Orcamento.objects.create(peca=pec,preco=prec)
    #if request.method == 'POST':
        #peca = request.POST.get('peca')
        #preco = request.POST.get('preco')

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
    