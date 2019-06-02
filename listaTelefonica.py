cont = 0
respAdc = 's'
respCons = 's'
respAlt = 's'
respDel = 's'
num = ''
contatos = {}
contatos2 = {}

print('BEM VINDO A LISTA TELEFÔNICA 2019\n')


while (cont == 0):
    #Repete o algoritmo por completo
    opc = input('DIGITE A OPÇÃO DESEJADA?\n1 para CADASTRAR\n2 para CONSULTAR\n3 para ALTERAR\n4 para EXCLUIR\n5 para VISUALIZAR TODOS OS CONTATOS\n0 para SAIR\n')
        # Mostra o menu para o usuário    

    if (opc == '1'):
        #Caso selecione a opção de cadastrar (1) //Menu principal
        print('CADASTRAR CONTATOS')
        if (respAdc != 's' or respAdc != 'S'):
            #se a resposta for positiva para "cadastrar"
            respAdc = 's'
                #a variavel "respADC" recebe 's'
        while (respAdc == 's' or respAdc == 'S'): 
            #enquanto respADC valer 's' será executado
            nome = input('Nome: ')
                #solicita ao usuário que digite o nome

            if (nome in contatos):
                #se o nome ja existir em "contatos"
                print('Este nome de contato já existe na agenda!')
                    #exibe essa mensagem
            else:
                #se não existir
                num = input('Número: ')
                    #pede para adicionar o número

                if (num in contatos.values()):
                    #se o numero ja existir
                    print('Este número já existe na agenda!')
                        #exibe essa mensagem
                else:
                    #se não existir
                    contatos[nome] = num
                        #Cadastra o nome como chave no dicionario "contatos"
                    contatos2[num] = nome
                        #cadastra o numero como chave no dicionario "contatos2"

            respAdc = input('\nDeseja adicionar mais um contato? S para sim e N para não: ')
                #Aqui se pergunta se o usuário quer continuar no menu "adicionar"
        
    elif (opc == '2'):
        #Caso selecione a opção de consultar (2) //Menu principal
        print('CONSULTAR CONTATOS')
        if (respCons != 's' or respCons != 'S'):
            #se a resposta for positiva para "consultar"
            respCons = 's'
                #a variavel "respCons" recebe 's'
        while (respCons == 's' or respCons == 'S'):
            #enquanto respCons valer 's' será executado
            tipoCons = int(input('Como deseja consultar?\n1 para consultar pelo NOME\n2 para consultar pelo NÚMERO\n'))
                #pergunta se o usuário deseja consultar pelo nome(1) ou pelo numero(2)

            if (tipoCons == 1):
                #se a resposta for positiva para "nome"
                cons = input('Digite o nome do contato\n')
                    #pede para digitar o nome
                print(contatos.get(cons, 'Contato não encontrado'))
                    #mostra o contato caso exista / caso não exista exibe uma mensagem de erro
            elif (tipoCons == 2):
                    #se a resposta for positiva para "numero"
                cons = input('Digite o número do telefone\n')
                    #pede para digitar o numero
                print(contatos2.get(cons, 'Contato não encontrado'))
                    #mostra o contato caso exista / caso não exista exibe uma mensagem de erro

            respCons = input('Deseja consultar outro contato? S para sim e N para não: ')
                #Aqui se pergunta se o usuário quer continuar no menu "consulta"
            
    elif (opc == '3'):
        #Caso selecione a opção de alterar (3) //Menu principal
        print('ALTERAR CONTATOS')
        #if (respAlt != 's' or respAlt != 'S'):
        #   respAlt = 's'
#q???
        while (respAlt == 's' or respAlt == 'S'):
            #repete a funcionalidade da opção
            #tipoCons = int(input('Deseja alterar o nome ou número?\n1 para o NOME\n2 para o NÚMERO\n'))

            #if (tipoCons == 1):
#q???
                cons = input('Digite o nome do contato\n')
                if (cons in contatos):
                    nome = input('Digite o novo nome\n')
                    contatos[nome] = contatos.pop(cons)
                else:
                    print('Contato não encontrado!\n')

                respCons = input('Deseja consultar outro contato? S para sim e N para não: ')
                    #Aqui se pergunta se o usuário quer continuar
#
#da uma atenção aq nessa opção
#
    elif(opc == '4'):
        #Caso selecione a opção de deletar (4) //Menu principal
        print('DELETAR CONTATOS')
        if (respDel != 's' or respDel != 'S'):
            #se a resposta for positiva para "deletar"
            respDel = 's'
                #a variavel "respDel" recebe 's'
        while (respDel == 's' or respDel == 'S'):
            #enquanto respDel valer 's' será executado
            tipoCons = int(input('Como deseja consultar?\n1 para consultar pelo NOME\n2 para consultar pelo NÚMERO\n'))
                #pergunta se o usuário deseja consultar pelo nome(1) ou pelo numero(2)
#consultar???
            if (tipoCons == 1):

                cons = input('Digite o nome do contato\n')
                print(contatos.pop(cons, 'Contato não encontrado'))
            elif (tipoCons == 2):
                cons = input('Digite o número do telefone\n')
                print(contatos.popitem(cons))

            respCons = input('Deseja consultar outro contato? S para sim e N para não: ')
                #Aqui se pergunta se o usuário quer continuar
    elif (opc == '5'):
        #Caso selecione a opção de excluir (5) //Menu principal
        sorted(contatos.values())
#q???
        for item in contatos.keys():
            print ("Nome: {0} | Telefone: {1}" .format(item, contatos[item]))
# q???    
    elif (opc == '0'):
        #Caso selecione a opção de sair (0)
        cont+=1
            #O contador do menu principal recebe +1 e encerra
    else:
        # Caso tenha digitado errado //Menu principal
        print('ERRO001: Opção inválida, favor tente novamente!')
            #Mensagem exibida caso tenha digitado errado
print('Obrigada por utilizar nosso programa!')
    #Mensagem de despedida ao encerrar o programa