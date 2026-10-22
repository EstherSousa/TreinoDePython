'''
Bloco 6: Questões 1 a 6:
(1) Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel 
[2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Com esses valores, faça um programa que calcule 
a média de gastos. Dica: use as funções built-in sum() e len().

(2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao 
total de compras.

(3) Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].

(4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.

(5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.

(6) Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.'''


#Questao 1
def q1():
    lista = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
    media = sum(lista)/len(lista)
    print(f"A media é igual a: {media}.")


#Questao 2
def q2():
    lista = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
    qtd = 0
    for valor in lista:
        if valor > 3000:
            qtd += 1
    porcentagem = (qtd*100)/len(lista)
    print(f"A porcentagem de valores acima de 3000 é {porcentagem}%.")


#Questao 3
import random

def q3():
    lista = []
    cont = 1
    while cont <= 5:
        valor = random.randint(1,1000)
        lista.append(valor)
        cont += 1
    print(lista)


#Questao 4
def q4():
    lista = []
    cont = 1
    while cont <= 5:
        valor = random.randint(1,1000)
        lista.append(valor)
        cont += 1
    print(lista)
    lista.reverse()
    print(lista)

from sympy import isprime, primerange


#Questao 5
def q5():
    valor = int(input("Digite um valor: "))
    '''primos = []
    for cont in range(1,(valor+1)):
       if isprime(cont):
        primos.append(cont)
    print(primos)'''
    primos2 = list(primerange(1, valor+1))
    print(primos2)
    


#Questao 6
from datetime import datetime

def q6():
    valor = input("Digite uma data, digite no formato 'dd/mm/aaaa': ")
    try:
        data = datetime.strptime(valor, "%d/%m/%Y")
        print("É valido.")
    except ValueError:
        print("Não é valido.") 



