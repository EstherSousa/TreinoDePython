'''Bloco 1: Questão 1: Crie um programa que solicite à pessoa usuária digitar seu nome, 
idade, altura em metros e peso em quilos e imprima “Olá, [nome], você tem [idade] anos, mede [altura] metros e pesa [peso] em quilos!”.'''

nome = input("Digite seu nome: ")
idade = int(input("Agora e sua idade: "))
altura = float(input("Agora, digite sua altura: "))
peso = float(input("E por ultimo, digite sua peso: "))

#Jeito N1
print(f"Olá, {nome}, você tem {idade} anos, mede {altura:.2f} metros e pesa {peso:.2f} quilos!")
#Jeito N2
print("Olá, %s, você tem %d anos, mede %.2f metros e pesa %.2f quilos!" %(nome, idade, altura, peso))
#Jeito N3
print("Olá, {}, você tem {} anos, mede {:.2f} metros e pesa {:.2f} quilos!" .format(nome, idade, altura, peso))
