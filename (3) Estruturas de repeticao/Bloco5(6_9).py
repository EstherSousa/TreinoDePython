'''
Bloco 5: Questões 6 a 9:
(6) Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, 
para o número 2, a tabuada deve ser mostrada no seguinte formato: 
Tabuada do 2:
2 x 1 = 2
2 x 2 = 4
[...]
2 x 10 = 20

(7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele 
que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

(8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma 
quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados 
com um número negativo.

(9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que 
calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira: 
- Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
- Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, 
deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.
'''


#Questao 6
def q6():
    valor = int(input("Digite um numero para realizar a tabuada: "))
    for numero in range(1,11):
        print (f"{valor} x {numero} = {valor*numero}")


#Questao 7
def q7():
    numero = int(input("Digite um numero para descobrir se é primo ou não: "))
    qtdDivisor = 0
    if numero == 1:
        qtdDivisor = 1
    for divisor in range(1,(numero//2) + 1):
        if numero%divisor == 0:
            qtdDivisor += 1
        if qtdDivisor >= 2 :
            print("Não é numero primo.")
            break
    if qtdDivisor == 1:
        print("É um numero primo.")


#Questao 8
def q8():
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    while True:
        idades = int(input("Digite idades uma por uma, caso queira que termine, digite um numero negativo: "))
        if idades < 0:
            break
        if (idades >= 0) and (idades <= 25):
            lista1.append(idades)
            continue
        if (idades >= 26) and (idades <= 50):
            lista2.append(idades)
            continue
        if (idades >= 51) and (idades <= 75):
            lista3.append(idades)
            continue
        if (idades >= 76) and (idades <= 100):
            lista4.append(idades)

    lista1.sort()
    lista2.sort()
    lista3.sort()
    lista4.sort()
    print(f"Idades de 0 a 25: {lista1}, idades de 26 a 50: {lista2}, idades de 51 a 75: {lista3} e idades de 76 a 100: {lista4}.")


#Questao 9
def q9():
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    candidato4 = 0
    nulo = 0
    branco = 0
    cont = 1
    while cont <= 20:
        voto = input("Digite entre os numeros de 1 a 6, sendo em ordem: 1 a 4 votos aos canditatos (1, 2, 3 e 4), 5 voto nulo e 6 voto em branco: ")
        match voto:
            case "1":
                candidato1 += 1
            case "2":
                candidato2 += 1
            case "3":
                candidato3 += 1
            case "4":
                candidato4 += 1
            case "5":
                nulo += 1
            case "6":
                branco += 1
            case _:
                print("Digite somente numeros entre 1 a 6, tente novamente.")
                continue
        cont += 1
    print(f"Quantidade de votos para o candidato 1: {candidato1}, Quantidade de votos para o candidato 2: {candidato2}, Quantidade de votos para o candidato 3: {candidato3}, Quantidade de votos para o candidato 4: {candidato4}, Quantidade de votos nulos: {nulo} e Quantidade de votos em branco: {branco}.")
    print(f"Porcentagem dos votos nulos: {nulo*5}% e porcentagem dos votos em brancos: {branco*5}%.")


    