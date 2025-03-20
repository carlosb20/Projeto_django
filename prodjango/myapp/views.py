from django.shortcuts import render

def index(request):

    text = {'val':'carlos'}
    
    return render(request,'myapp/index.html' , text)


def contato(request):
    return render(request,'myapp/contato.html')