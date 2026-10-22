"""Bloco 2: Questões 1 a 8 (Menos a (2)): Crie um programa que solicite dois valores numéricos à pessoa usuária e 
(1) Imprima a soma dos dois valores.
(2) Solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
(3) Imprima a subtração do primeiro pelo o segundo valor.
(4) Imprima a multiplicação dos dois valores.
(5) Um operador e uma potência, e realize a exponenciação entre esses dois valores.
(6) Um numerador e um denominador, e realize a divisão entre os dois valores.
(7) Um numerador e um denominador e realize a divisão inteira entre os dois valores. 
(8) Um numerador e um denominador, e retorne o resto da divisão entre os dois valores. 
Deixe claro que o valor do denominador não pode ser 0. (Serve para os 3 ultimo)"""

#Questao 1
print("Digite 2 numeros para soma.")
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Agora, Digite o segundo numero: "))
print(f"A soma deles é: {(numero1 + numero2):.2f}")

#Questao 2
print("Digite 3 numeros para soma.")
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Agora, Digite o segundo numero: "))
numero3 = float(input("E por ultimo, Digite o terceiro numero: "))
print(f"A soma deles é: {((numero1 + numero2) + numero3):.2f}")

#Questao 3
print("Digite 2 numeros para subtração do primeiro pelo o segundo valor.")
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Agora, Digite o segundo numero: "))
print(f"A subtração deles é: {(numero1 - numero2):.2f}")

#Questao 4
print("Digite 2 numeros para multiplicação.")
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Agora, Digite o segundo numero: "))
print(f"A multiplicação deles é: {(numero1 * numero2):.2f}")

#Questao 5
print("Digite 2 numeros, Um operador e uma potência, para realizar a exponenciação entre eles.")
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Agora, Digite o segundo numero: "))
print(f"A potenciação deles é: {(numero1 ** numero2):.2f}")

#Questao 6
print("Digite 2 numeros, Um numerador e um denominador, para realizar a divisão entre eles. O valor do denominador não pode ser 0.")
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Agora, Digite o segundo numero: "))
print(f"A divisão deles é: {(numero1 / numero2):.2f}")

#Questao 7
print("Digite 2 numeros, Um numerador e um denominador, para realizar a divisão inteira entre eles. O valor do denominador não pode ser 0.")
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Agora, Digite o segundo numero: "))
print(f"A divisão inteira deles é: {numero1 // numero2}")

#Questao 8
print("Digite 2 numeros, Um numerador e um denominador, para retornar o resto da divisão entre eles. O valor do denominador não pode ser 0.")
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Agora, Digite o segundo numero: "))
print(f"O resto deles é: {numero1 % numero2}")