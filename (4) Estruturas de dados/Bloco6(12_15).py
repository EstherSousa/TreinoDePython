'''
Bloco 6: Questões 12 a 15:
(12) Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos 
computados podem ser observados abaixo:

Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos
Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.

(13) As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do salário devido ao ótimo 
desempenho do time. O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos 
recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: 
[1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. O abono de cada colaborador(a) não pode ser inferior a 200. 
Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos 
com o abono, quantos(as) colaboradores(as) receberam o abono mínimo e qual o maior valor de abono fornecido.

(14) Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. A equipe fez a coleta de informações sobre o 
número de espécies de plantas e animais em cada área dessa floresta e armazenou essas informações em um dicionário. Nele, a chave descreve a 
área dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.
{'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}
Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica. Dica: use as funções 
built-in sum() e len().

(15) O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa. Para isso, foram 
fornecidos os seguintes dados:
{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre 
todos os setores e quantas pessoas estão acima da idade média geral.'''


#Questao 12
def q12():
    tab = {'Design 1': 1334,'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811 }
    soma = sum(tab.values())
    maior_valor = max(tab.values())
    for chave, valor in tab.items():
        if valor == maior_valor:
            porcentagem = (valor*100)/soma
            print(f"O vencedor foi o {chave}, com {porcentagem:.2f}% dos votos totais.")


#Questao 13
def q13():
    salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
    abonos = []
    cont = 0
    for valor in salarios:
        abono = valor/10
        if abono < 200:
            abono = 200
            cont += 1
        abonos.append(abono)
    soma = sum(abonos)
    valor_max = max(abonos)
    dici = dict(zip(salarios,abonos))
    print(dici)
    print(soma,cont,valor_max)


#Questao 14
def q14():
    dici = {'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}
    valores = dici.values()
    for var in valores:
        media = sum(var)/len(var)
    '''AINDA NÃO FOI TERMINADO pois não entendi a questão.'''


#Questao 15
def q15():
    dici = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65], 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64], 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56], 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]} 
    medias_idades = []
    cont = 0
    valores = dici.values()
    for var in valores:
        media = sum(var)/10
        medias_idades.append(media)
    media_total = sum(medias_idades)/len(medias_idades)
    for var2 in valores:
        for var3 in var2:
            if var3 > media_total:
                cont += 1
    print(valores)
    print(medias_idades)
    print(media_total, cont)


            

