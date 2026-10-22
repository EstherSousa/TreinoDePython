'''
Bloco 4: Questões 1 a 9:
(1) Escreva um programa que peça ao usuário fornecer dois números e exibir o número maior.
(2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e 
informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).
(3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.
(4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e 
exiba o valor mais alto e mais baixo entre esses três anos.
(5) Escreva um programa que pergunte sobre o preço de três produtos e 
indique qual é o produto mais barato para comprar.
(6) Escreva um programa que leia três números e os exiba em ordem decrescente.
(7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite")
 e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
(8) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar.
(9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.'''

#Questao 1
def q1():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))

    if num1 > num2:
        print(f"O primeiro numero: {num1} é maior que o segundo numero: {num2}.")
    elif num1 < num2:
        print(f"O segundo numero: {num2} é maior que o primeiro numero: {num1}.")
    else:
        print("Os dois numeros são iguais.")

#Questao 2
def q2():
    per = float(input("Digite o percentual de crescimento de produção da empresa: "))

    if per > 0:
        print("Houve um crescimento na produção.")
    elif per < 0:
        print("Houve um decrescimento na produção.")
    else:
        print("Não houve mudança alguma na produção.")

#Questao 3
def q3():
    vogal = ["A", "E", "I", "O", "U", "Y"]

    letra = input("Digite uma letra: ")
    letra.upper()

    if letra.isalpha() == False:
        print("Não é uma letra do alfabeto.")
    elif (letra in vogal):
        print("Esta letra é uma vogal.")
    else:
        print("Esta letra é uma consoante.")

#Questao 4
def q4():
    precosTotal = []

    for valor in range(0,3):
        preco = float(input(f"Digite os 3 valores medio do preço do modelo do carro durante os 3 anos na ordem({valor + 1}): "))
        precosTotal.append(preco)
    maior = max(precosTotal)
    menor = min(precosTotal)
    print(f"O valor mais alto é {maior}, e o menor é {menor}.")

#Questao 5
def q5():
    precosTotal = []

    for valor in range(0,3):
        preco = float(input(f"Digite o preço dos 3 produtos, produto de numero:{valor + 1}: "))
        precosTotal.append(preco)

    menor = min(precosTotal)
    posicao = precosTotal.index(menor)

    if posicao == 0:
        print("O primeiro produto é o mais barato.")
    if posicao == 1:
        print("O segundo produto é o mais barato.")
    if posicao == 2:
        print("O terceiro produto é o mais barato.")

#Questao 6
def q6():
    numerosTotal = []

    for valor in range(0,3):
        numero = int(input(f"Digite um valor no total de 3, numero de ordem {valor + 1}: "))
        numerosTotal.append(numero)
    
    numerosTotal.sort()
    numerosTotal.reverse()

    print(f"Os numeros em ordem decrescente: {numerosTotal}")

#Questao 7
def q7():
    turno = input("Qual o turno em que você estuda: manhã, tarde ou noite? Digite uma das 3 opções: ")

    match turno:
        case "manhã":
            print("Bom Dia!")
        case "tarde":
            print("Boa Tarde!")
        case "noite":
            print("Boa Noite!")
        case _:
            print("Valor Inválido!")

#Questao 8
def q8():
    num = int(input("Digite um numero: "))

    if num == 0:
        print("O numero nem é par ou impar, ele é igual a zero.")
    elif (num % 2) == 0:
        print("O numero é par.")
    else:
        print("O numero é impar.")

#Questao 9
def q9():
    num = float(input("Digite um numero: "))

    inteiro = int(num)

    if num - inteiro != 0:
        print("O numero é decimal.")
    else:
        print("O numero é inteiro.")

