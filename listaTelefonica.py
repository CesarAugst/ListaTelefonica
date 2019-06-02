cont = 0
respAdc = 's'
respCons = 's'
respAlt = 's'
respDel = 's'
num = ''
contatos = {}

print('BEM VINDO A LISTA TELEFÔNICA 2019\n')


while (cont == 0):
# Repete o algoritmo todo
    opc = input('DIGITE A OPÇÃO DESEJADA?\n1 para CADASTRAR\n2 para CONSULTAR\n3 para ALTERAR\n4 para EXCLUIR\n5 para VISUALIZAR TODOS OS CONTATOS\n0 para SAIR\n')

    if (opc == '1'):
        print('CADASTRAR CONTATOS')
        if (respAdc != 's' or respAdc != 'S'):
            respAdc = 's'
        while (respAdc == 's' or respAdc == 'S'): 
            nome = input('Nome: ')

            if (nome in contatos):
                print('Este nome de contato já existe na agenda!')
            else:
                num = input('Número: ')

                if (num in contatos.values()):
                    print('Este número já existe na agenda!')
                else:
                    contatos[nome] = num

            respAdc = input('\nDeseja adicionar mais um contato? S para sim e N para não: ')
        
    elif (opc == '2'):
        #Caso escoilhida a segunda opção
        print('CONSULTAR CONTATOS')
        if (respCons != 's' or respCons != 'S'):
            respCons = 's'
        while (respCons == 's' or respCons == 'S'):
        #repete a funcionalidade da opção
            tipoCons = int(input('Como deseja consultar?\n1 para consultar pelo NOME\n2 para consultar pelo NÚMERO\n'))

            if (tipoCons == 1):
                cons = input('Digite o nome do contato\n')
                print(contatos.get(cons, 'Contato não encontrado'))
            elif (tipoCons == 2):
                cons = input('Digite o número do telefone\n')
                print(contatos.get(cons, 'Contato não encontrado'))

            respCons = input('Deseja consultar outro contato? S para sim e N para não: ')
            # Pergunta se quer continuar
            
    elif (opc == '3'):
        print('ALTERAR CONTATOS')
        #if (respAlt != 's' or respAlt != 'S'):
         #   respAlt = 's'
        while (respAlt == 's' or respAlt == 'S'):
        #repete a funcionalidade da opção
            #tipoCons = int(input('Deseja alterar o nome ou número?\n1 para o NOME\n2 para o NÚMERO\n'))

            #if (tipoCons == 1):
                cons = input('Digite o nome do contato\n')
                if (cons in contatos):
                    nome = input('Digite o novo nome\n')
                    contatos[nome] = contatos.pop(cons)
                else:
                    print('Contato não encontrado!\n')
            ''' elif (tipoCons == 2) 
                cons = input('Digite o número de telefone\n')
                if (cons in contatos.values()):
                    num = input('Digite o novo número de telefone\n')
                    nome = [contatos for contatos, name in contatos.items() if name == num]
                    print(nome)
                    #contatos[] = num
                else:
                    print('Contato não encontrado!\n')
            else:
                print('Opção Inválida\n') '''
                

            respCons = input('Deseja consultar outro contato? S para sim e N para não: ')
            # Pergunta se quer continuar
    elif (opc == '4'):
        print('DELETAR CONTATOS')
        if (respDel != 's' or respDel != 'S'):
            respDel = 's'
        while (respDel == 's' or respDel == 'S'):
        #repete a funcionalidade da opção
            tipoCons = int(input('Como deseja consultar?\n1 para consultar pelo NOME\n2 para consultar pelo NÚMERO\n'))

            if (tipoCons == 1):
                cons = input('Digite o nome do contato\n')
                print(contatos.pop(cons, 'Contato não encontrado'))
            elif (tipoCons == 2):
                cons = input('Digite o número do telefone\n')
                print(contatos.popitem(cons))

            respCons = input('Deseja consultar outro contato? S para sim e N para não: ')
            # Pergunta se quer continuar
    elif (opc == '5'):
        sorted(contatos.values())
        for item in contatos.keys():
            print ("Nome: {0} | Telefone: {1}" .format(item, contatos[item]))
    
    elif (opc == '0'):
        cont+=1
    else:
    # Caso tenha digitado errado
        print('ERRO001: Opção inválida, favor tente novamente!')
print('Obrigada por utilizar nosso programa!')