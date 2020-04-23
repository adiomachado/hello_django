from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {}</h1>'.format(nome, idade))

"""
Exercicio 1:
Criar uma rota que aceite mais dois parâmetros do tipo inteiro e retorne a soma destes valores
Criar rotas para as quatro operações básicas
"""
 
def soma(request, valor1, valor2):
    total = valor1 + valor2
    return HttpResponse('<h1>Resultado Soma: {} </h1>'.format(total))

def subtracao(request, valor1, valor2):
    if valor1 >= valor2:
        total = valor1 - valor2
    else:
        total = valor2 - valor1
    return HttpResponse('<h1>Resultado subtração: {} </h1>'.format(total))

def multiplica(request, valor1, valor2):
    total = valor1 * valor2
    return HttpResponse('<h1>Resultado Multiplicação: {} </h1>'.format(total))

def divisao(request, valor1, valor2):
    total = valor1 / valor2
    return HttpResponse('<h1>Resultado Divisão: {} </h1>'.format(total))
