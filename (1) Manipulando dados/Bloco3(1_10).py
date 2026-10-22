"""Bloco 3: Questões 1 a 9:
(1) Crie uma variável chamada “frase”, atribua a ela uma string de sua escolha, 
e imprima a frase na tela e deixe a frase sem espaços em branco no início e no fim.

Crie um código que solicite uma frase e
(2) Depois imprima a frase na tela.
(3) Imprima a mesma frase digitada mas com todas as letras maiúsculas.
(4) Imprima a mesma frase digitada mas com todas as letras minúsculas.
(5) Imprima a mesma frase sem espaços em branco no início e no fim.
(6) Imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas. 
(7) Imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”. 
(8) Imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
(9) Imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”."""


#Questao 1
frase = " Meu gato é lindo. "
frase = frase.strip()
print (frase)

#Questao 2
fraseDoUsuario = input("Escreva uma frase: ")
print(fraseDoUsuario)
fraseDoUsuarioCopia = fraseDoUsuario

#Questao 3
fraseDoUsuario = fraseDoUsuario.upper()
print(fraseDoUsuario)

#Questao 4
fraseDoUsuario = fraseDoUsuario.lower()
print(fraseDoUsuario)

#Questao 5
fraseDoUsuario = fraseDoUsuario.strip()
print(fraseDoUsuario)

#Codigo extra:
fraseDoUsuario = fraseDoUsuario.upper()
print(fraseDoUsuario)

#Questao 6
fraseDoUsuario = fraseDoUsuario.strip().lower()
print(fraseDoUsuario)

fraseDoUsuario = fraseDoUsuarioCopia

#Questao 7
fraseDoUsuario = fraseDoUsuario.replace('e','f')
fraseDoUsuario = fraseDoUsuario.replace('E','F')
print(fraseDoUsuario)

fraseDoUsuario = fraseDoUsuarioCopia

#Questao 8
fraseDoUsuario = fraseDoUsuario.replace('a','@')
fraseDoUsuario = fraseDoUsuario.replace('A','@')
print(fraseDoUsuario)

fraseDoUsuario = fraseDoUsuarioCopia

#Questao 9
fraseDoUsuario = fraseDoUsuario.replace('s','$')
fraseDoUsuario = fraseDoUsuario.replace('S','$')
print(fraseDoUsuario)

#Metodos para Strings:

'''UPPER'''
print("\nFaz todas as letras maiusculas\n")
frase1 = "estudo de python"
print(frase1.upper())

'''LOWER'''
print("\nFaz todas as letras minusculas\n")
frase2 = "ESTUDO DE PYTHON"
print(frase2.lower())

'''LEN'''
print("\nTamanho da string\n")
frase3 = "Estudo de Python"
print(len(frase3))

'''CAPITALIZE'''
print("\nPrimeira letra em maiusculo e resto minusculo\n")
frase4 = "estudo de python"
print(frase4.capitalize())

'''FIND'''
print("\nO índice da primeira ocorrência de um texto na string\n")
frase5 = "Estudo de Python"
print(frase5.find("t"))

'''TITLE'''
print("\nPrimeira letra de cada palavra em maiúscula\n")
frase6 = "estudo de python"
print(frase6.title())

'''COUNT'''
print("\nNúmero de vezes que um determinado valor aparece na string\n")
frase7 = "Estudo de python e de estetica"
print(frase7.count("e"))

'''ISUPPER'''
print("\nRetorna True se todas as letras na string estiverem em maiúsculas\n")
frase8 = "ESTUDO DE PYTHON  "
print(frase8.isupper())

#Codigo extra:
frase8_5 = "ESTUDO de PYTHON"
print(frase8_5.isupper())

'''ISLOWER'''
print("\nRetorna True se todas as letras na string estiverem em minusculos\n")
frase9 = "estudo de python"
print(frase9.islower())

#Codigo extra:
frase9_5 = "estudo DE python"
print(frase9_5.islower())

'''STARTSWITH'''
print("\nRetorna True se a string inicia com uma determinada sequência\n")
frase10 = "Estudo de python"
print(frase10.startswith("Est"))

#Codigo extra:
frase10_5 = "Estudo de python"
print(frase10_5.startswith("E5t"))

'''ENDSWITH'''
print("\nRetorna True se a string termina com uma determinada sequência\n")
frase11 = "Estudo de python"
print(frase11.endswith("hon"))

#Codigo extra:
frase11_5 = "Estudo de python"
print(frase11_5.endswith("han"))

'''ISALNUM'''
print("\nRetorna True se a string possui algum elemento alfabetico e numerico\n")
frase12 = "!@#$5b&"
print(frase12.isalnum())

#Codigo extra:
frase12_5 = "!@#$&"
print(frase12_5.isalnum())

'''ISALPHA'''
print("\nRetorna True se a string possui somente elementos alfabeticos\n")
frase13 = "Estudo de python"
print(frase13.isalpha())

#Codigo extra:
frase13_5 = "Estudo 33 python"
print(frase13_5.isalpha())

'''SWAPCASE'''
print("\nInverte o conteudo da string (Maiusculo/Minusculo)\n")
frase14 = "Estudo de Python"
print(frase14.swapcase())

'''SPLIT'''
print("\nTransforma a string em uma lista ultilizando os espaços como referencia\n")
frase15 = "Estudo de python"
print(frase15.split())

'''REPLACE'''
print("\nSubstitui na string o trecho 'S1' pelo trecho 'S2' replace(S1,S2)\n")
frase16 = "Estudo de python"
print(frase16.replace("python", "pato"))

'''LJUST'''
print("\nAjusta o tamanho minimo de uma string, acrescentando pela direita se necessario\n")
frase17 = "Estudo de python"
print(frase17.ljust(22))

#Codigo extra:
frase17_5 = "Estudo de python"
print(frase17_5.ljust(12))

'''RJUST'''
print("\nAjusta o tamanho minimo de uma string, acrescentando pela esquerda se necessario\n")
frase18 = "Estudo de python"
print(frase18.rjust(22))

#Codigo extra:
frase18_5 = "Estudo de python"
print(frase18_5.rjust(12))

'''CENTER'''
print("\nAjusta o tamanho minimo de uma string, acrescentando pela direita e esquerda se necessario\n")
frase19 = "Estudo de python"
print(frase19.center(22))

#Codigo extra:
frase19_5 = "Estudo de python"
print(frase19_5.center(12))

'''LSTRIP'''
print("\nRemove todos os espaços em branco no lado da esquerdao\n")
frase20 = "       Estudo de python"
print(frase20.lstrip())

'''RSTRIP'''
print("\nRemove todos os espaços em branco no lado da direita\n")
frase21 = "Estudo de python       "
print(frase21.rstrip())

'''STRIP'''
print("\nRemove todos os espaços em branco\n")
frase22 = "  Estudo de python   "
print(frase22.strip())


#Caracteres Especiais num print

print("O caracter (barra n) faz pular a linha \n tipo assim.\n")
print("O caracter (barra t)\tadiciona um espaço de tabulação \n tipo dessa forma\tcomo uma tabela.\n")
print("Colocando (duas barras juntas) faz a barra \\ aparecer no texto.\n")
print("Colocando (barra e aspas) faz as \"aspas\" aparecerem no texto.\n")
print('Colocando (barra e aspas) faz as \'aspas\' aparecerem no texto.')