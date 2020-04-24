from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {}</h1>'.format(nome, idade))

"""
Exercicio 1:
Criar uma rota que aceite mais dois parâmetros do tipo inteiro e retorne a soma destes valores
Criar rotas para as quatro operações básicas
Aqui faço apenas um método e uma rota em urls.py. A chamada é feita com: 
127.0.0.1:8000/calcula/soma/10/20 informando o metodo calcula e o tipo da operacao: soma, subtracao, 
multiplicacao ou divisao e os dois valores, retorna o resultado da respectiva operação.
"""
def calcula(request, tipo, valor1, valor2):
    if tipo == 'soma':
        total = valor1 + valor2
        operacao = 'Soma: '
    elif tipo == 'subtracao':
        total = valor1 - valor2
        operacao = 'Subtração: '
    elif tipo == 'multiplicacao':
        total = valor1 * valor2
        operacao = 'Multiplicação: '
    else:
        total = valor1 / valor2
        operacao = 'Divisão: '
    return HttpResponse(f'<h1>Resultado ' + operacao + format(total) + '</h1>')

"""   
Exemplo de como chamar a rota para cada operacao. 127.0.0.1:8000/soma/10/20
irá somar 10 + 20 e retornar 30
tem que fazer uma rota para cada método, só deixei como exemplo
     
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
"""
