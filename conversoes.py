print('BEM VINDO AO CONVERSOR!')
tipoConv = 21

while (tipoConv != 0):
    tipoConv = int(input('Deseja converter moedas ou medidas?\n1 - MOEDAS\n2 - MEDIDAS\n0 - SAIR\n'))

    if(tipoConv == 1):
        tipoConvMo = int(input('Deseja converter\n1 - REAL para DÓLAR\n2 - DÓLAR para REAL\n'))
        if (tipoConvMo == 1):
            real = float(input('Qual é o valor em real?\nR$'))
            cotacao = float(input('Qual é o valor da cotação atual?\n'))

            dolar = real / cotacao

            print('\nR${} equivale a U${} com a cotação de {}\n'.format(real, dolar, cotacao))
            input('\nENTER para continuar\n')

        elif (tipoConvMo == 2):
            dolar = float(input('Qual é o valor em dolar?\nU$'))
            cotacao = float(input('Qual é o valor da cotação atual?\n'))

            real = dolar * cotacao

            print('\nU${} equivale a R${} com a cotação de {}\n'.format(dolar, real, cotacao))
            input('\nENTER para continuar\n')

    elif(tipoConv == 2):
        tipoConvMetro = int(input('Deseja converter\n1 - KM para MILHAS\n2 - MILHAS para KM\n'))
        if (tipoConvMetro == 1):
            km = float(input('Qual é o valor em KM?\n'))

            milha = km / 1.609

            print('\n{} km equivale a {} milhas\n'.format(km, milha))
            input('\nENTER para continuar\n')

        elif (tipoConvMetro == 2):
            milha = float(input('Qual é o valor em milhas?\n'))

            km = milha * 1.609

            print('{} milhas equivale a {} km'.format(milha, km))
            input('\nENTER para continuar\n')

print('\nObrigada por utilizar nosso programa!')