'''
Bloco 6: Questões 7 a 11:
(7) Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias por dia (em milhares) 
e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista 
contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia 
anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).

(8) Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID 
par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e 
amargos.

(9) Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para 
cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.
Gabarito da prova:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B

(10) Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que 
colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima 
da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).

(11) Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:
{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
 Escreva um código que calcule o total de vendas e o produto mais vendido.'''


#Questao 7
def q7():
    num_bac = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
    porcent_lista = []
    for idx in range(1, len(num_bac)):
        am_at = num_bac[idx]
        am_an = num_bac[idx-1]
        porcent = (100*(am_at - am_an)) / am_an
        porcent_lista.append(porcent)
    print([f"{v:.2f}" for v in porcent_lista])


#Questao 8
import random

def q8():
    produtos = []
    doces = 0
    amargos = 0
    for idx_qtd in range(1,11):
        ID = random.randint(1,100)
        produtos.append(ID)
    print(produtos)
    for valor in produtos:
        if valor%2 == 0:
            doces = doces + 1
        else:
            amargos = amargos + 1
    print(f"Há {doces} produtos doces, e {amargos} produtos amargos.")


#Questao 9
def q9():
    print("Responda as 10 questões seguintes, cada uma entre as alternativas A, B, C e D, diferente disso a questão será dada como errada.")
    gabarito_prova = ["D","A","C","B","A","D","C","C","A","B"]
    nota = 0
    questao = 1
    for gabarito in gabarito_prova:
        resposta = input(f"Digite entre as alternativas [A,B,C,D] a resposta da questão {questao}: ")
        questao = questao + 1
        if resposta == gabarito:
            nota = nota + 1
    print(nota)


#Questao 10
def q10():
    posicao = 0
    temp_medias = []
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    for mes in meses:
        temperatura = float(input(f"Digite qual foi a temperatura media referente do mês {mes}: "))
        temp_medias.append(temperatura)
    temp_anual = sum(temp_medias)/len(temp_medias)
    print(temp_anual)
    for valor in temp_medias:
        if valor > temp_anual:
            print(meses[posicao])
        posicao += 1


#Questao 11
def q11():
    dici = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
    soma = sum(dici.values())
    maior_valor = max(dici.values())
    for chave, valor in dici.items():
        if valor == maior_valor:
            print(chave,soma)





