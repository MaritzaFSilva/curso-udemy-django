from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    sexo ='m'
    nome = 'Alfredo'
    lista =[
        {'nome': 'Pedro', 'sexo':'m'},
        {'nome': 'Maria', 'sexo':'f'},
        {'nome': 'José', 'sexo':'m'},
        {'nome': 'Ana', 'sexo':'f'},
    ]
    return render(request,'index.html',{'lista': lista, 'sexo': sexo, 'nome': nome})


