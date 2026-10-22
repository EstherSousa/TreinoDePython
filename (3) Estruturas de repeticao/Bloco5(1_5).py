'''
Bloco 5: Questões 1 a 5:
(1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

(2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, 
com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.

(3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas 
são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido 
uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.

(4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada 
ao ser enviado o valor -273°C.

(5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando que o fatorial de um número 
inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.'''


#Questao 1
def q1():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Agora digite o segundo numero: "))

    for valor in range(num1 + 1, num2):
        print (valor)


#Questao 2
def q2():
    A = 4
    B = 10
    dias = 0
    while A < B:
        A = A*1.03
        B = B*1.015
        dias += 1
    print (f"Passou {dias} dias para colonia de bacteria A superou ou se igualou a colonia de bacteria B.")


#Questao 3
def q3():
    valores = []
    posicao = 1
    while True:
        nota = int(input(f"Digite entre 0 e 5 para ser a nota do usuario {posicao}°: "))
        if nota < 0 or nota > 5:
            print("Só pode numeros entre 0 e 5, tente novamente.")
            continue
        valores.append(nota)
        posicao +=1
        if posicao == 16:
            break


#Questao 4
def q4():
    conjunto = []
    soma = 0
    while True:
        temperatura = int(input("Digite uma temperatura, caso queira terminar, digite -273: "))
        if temperatura == -273:
            break
        conjunto.append(temperatura)
    for valores in conjunto:
        soma += valores
    media = soma/len(conjunto)
    print(f"A media das temperaturas é {media}.")


#Questao 5
def q5():
    valor = int(input("Digite um valor para ser fatorado: "))
    fatorial = 1
    while True:
        fatorial *= valor
        valor -= 1
        if valor <= 0:
            break
    print (f"O fatorial do valor é: {fatorial}.")

