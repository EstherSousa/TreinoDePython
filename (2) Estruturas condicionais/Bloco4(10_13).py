'''
Bloco 4: Questões 10 a 13:
(10) Um programa deve ser escrito para ler dois números e,
em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. 
O resultado da operação deve incluir informações sobre o número - 
se é par ou ímpar, positivo ou negativo e inteiro ou decimal.
 
(11) Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo.
O programa deve informar se os valores podem ser utilizados para formar um triângulo 
e, caso afirmativo, se ele é equilátero, isósceles ou escaleno.
(Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes.)

(12) Um estabelecimento está vendendo combustíveis com descontos variados. 
Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. 
Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros,
o desconto será de 3% por litro. Caso contrário, será de 5% por litro. 
O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. 
Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível 
(E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente.
(-O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros 
e o valor do desconto.
-O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela 
quantidade de litros menos o valor de desconto resultante do cálculo.)

(13) Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais
para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda
durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação,
deve ser enviada às seguintes sugestões:
Para variação acima de 20%: bonificação para o time de vendas.
Para variação entre 2% e 20%: pequena bonificação para time de vendas.
Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
Para variação abaixo de -10%: corte de gastos.'''


#Questao 10
def q10():
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))

    operacao = int(input("Escolha entre 1 e 4, sendo em ordem, Adição, Subtração, Multiplicação e Divisão: "))

    match operacao:
        case 1:
            resultado = num1 + num2
        case 2:
            resultado = num1 - num2
        case 3:
            resultado = num1 * num2
        case 4:
            if num2 == 0:
                print("Não é possivel uma divisão por 0.")
                return
            resultado = num1 / num2
        case _:
            print("Valor invalido!")

    print(f"E o resultado deu {resultado}. Já sobre o resultado: ")

    if resultado == 0:
        print("Como o resultado deu zero, ou seja, ele não é par nem impar, nem possitivo, nem negativo e é inteiro.")
        return
    
    inteiro = int(resultado)

    if (resultado % 2) == 0:
        print("O resultado é par.")
    else:
        print("O resultado é impar.")

    if resultado > 0:
        print("O resultado é positivo.")
    else:
        print("O resultado é negativo.")
    
    if resultado - inteiro != 0:
        print("O resultado é decimal.")
    else:
        print("O resultado é inteiro.")


#Questao 11
def q11():
    lado1 = int(input("Dê o valor do primeiro lado: "))
    lado2 = int(input("Dê o valor do segundo lado: "))
    lado3 = int(input("Dê o valor do terceiro lado: "))

    if ((lado1 + lado2) > lado3) and ((lado1 + lado3) > lado2) and ((lado2 + lado3) > lado1):
        if lado1 == lado2 == lado3:
            print("É um Triangulo Equilátero.")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("É um Triangulo Isósceles.")
        else:
            print("É um Triangulo Escaleno.")
    else:
        print("Não é um Triangulo.")

#Questao 12
def q12():
    etanol = {'preco':1.70,'desconto1':0.02,'desconto2':0.04}
    diesel = {'preco':2.00,'desconto1':0.03,'desconto2':0.05}

    tipo = input("Escolha o tipo de combustivel, entre 'E' de Etanol e 'D' de Diesel. Digite sua opção: ")
    qtd = int(input("Agora digite a quantidade de litros a ser calculado: "))

    match tipo:
        case 'E':
            if qtd <= 15:
                desconto = (etanol.get('preco') * qtd) * etanol.get('desconto1')
            else:
                desconto = (etanol.get('preco') * qtd) * etanol.get('desconto2')

            valor = (etanol.get('preco') * qtd) - desconto

        case 'D':
            if qtd <= 15:
                desconto = (diesel.get('preco') * qtd) * diesel.get('desconto1')
            else:
                desconto = (diesel.get('preco') * qtd) * diesel.get('desconto2')
                
            valor = (diesel.get('preco') * qtd) - desconto

        case _:
            print("Valor invalido.")

    print(f"O valor final é: {valor:.2f} reais.")


#Questao 13
def q13():
    numVendas22 = int(input("Digite a quantidade de vendas do ano de 2022: "))
    numVendas23 = int(input("Digite a quantidade de vendas do ano de 2023: "))

    varPer = ((numVendas23 - numVendas22) / numVendas22) * 100

    if varPer > 20:
        print("Como sugestão: Bonificação para o time de vendas.")
    elif 20 >= varPer >= 2:
        print("Como sugestão: Pequena bonificação para time de vendas.")
    elif 2 > varPer >= -10:
        print("Como sugestão: Planejamento de políticas de incentivo às vendas.")
    else:
        print("Como sugestão: Corte de gastos.")



