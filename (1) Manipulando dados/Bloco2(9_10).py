'''Bloco 2: Questões 9 e 10: 
(9) Crie um código que solicita 3 notas de um estudante e imprima a média das notas. 
(10) Crie um código que calcule e imprima a média ponderada dos números 
5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.'''

#Questao 9
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = ((nota1 + nota2) + nota3) / 3
print(media)

#Questao 10
media_ponderada = (5.0*1 + 12.0*2 + 20.0*3 + 15.0*4) / 10
print(media_ponderada)