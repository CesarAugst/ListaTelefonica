cont = 0
respAdc = 's'
respCons = 's'
respAlt = 's'
respDel = 's'
num = ''
contatos = {}
contatos2 = {}

print('\nBEM VINDO A LISTA TELEFÔNICA 2019\n')

# Repete o algoritmo por completo
while (cont == 0):
    # Mostra o menu para o usuário   
    opc = int(input('\nDIGITE A OPÇÃO DESEJADA?\n1 para CADASTRAR\n2 para CONSULTAR\n3 para ALTERAR\n4 para EXCLUIR\n5 para VISUALIZAR TODOS OS CONTATOS\n0 para SAIR\n'))

    # Caso selecione a opção de cadastrar (1) //Menu principal
    if (opc == 1):
        print('\nCADASTRAR CONTATOS')
        # Se a resposta for negativa para "cadastrar"
        if (respAdc != 's' or respAdc != 'S'):
            # A variavel "respADC" recebe 's'
            respAdc = 's'
        # Enquanto respADC valer 's' será executado
        while (respAdc == 's' or respAdc == 'S'): 
            # Solicita ao usuário que digite o nome
            nome = input('\nNome: ')
            # Se o nome ja existir em "contatos"
            if (nome in contatos):
                # Exibe essa mensagem
                print('\nEste nome de contato já existe na agenda!\n')
            # Se não existir
            else:
                # Pede para adicionar o número
                num = input('Número: ')
                # Se o numero ja existir
                if (num in contatos.values()):
                    # Exibe essa mensagem
                    print('Este número já existe na agenda!')
                # Se não existir    
                else:
                    # Cadastra o nome como chave no dicionario "contatos"
                    contatos[nome] = num
                    # Cadastra o numero como chave no dicionario "contatos2"
                    contatos2[num] = nome       
            # Aqui se pergunta se o usuário quer continuar no menu "adicionar"
            respAdc = input('\n\nDeseja adicionar mais um contato? S para sim e N para não: ')
                
    # Caso selecione a opção de consultar (2) //Menu principal
    elif (opc == 2):
        print('\nCONSULTAR CONTATOS')
        # Se a resposta for negativa para "consultar"
        if (respCons != 's' or respCons != 'S'):
            # A variavel "respCons" recebe 's'
            respCons = 's'
        # Enquanto respCons valer 's' será executado        
        while (respCons == 's' or respCons == 'S'):
            # Pergunta se o usuário deseja consultar pelo nome(1) ou pelo numero(2)
            tipoCons = int(input('\nComo deseja consultar?\n1 para consultar pelo NOME\n2 para consultar pelo NÚMERO\n'))
                
            # Se a resposta for positiva para "nome"
            if (tipoCons == 1):
                # Pede para digitar o nome
                cons = input('\nDigite o nome do contato\n')
                # Mostra o contato caso exista / caso não exista exibe uma mensagem de erro    
                print(contatos.get(cons, 'Contato não encontrado'))
            # Se a resposta for positiva para "numero"        
            elif (tipoCons == 2):
                # Pede para digitar o numero    
                cons = input('\nDigite o número do telefone\n')
                # Mostra o contato caso exista / caso não exista exibe uma mensagem de erro    
                print(contatos2.get(cons, 'Contato não encontrado'))
                    
            # Aqui se pergunta se o usuário quer continuar no menu "consulta"
            respCons = input('\nDeseja consultar outro contato? S para sim e N para não: ')
                
    # Caso selecione a opção de alterar (3) //Menu principal
    elif (opc == 3):
        print('\nALTERAR CONTATOS')
        # Se a resposta for negativa para "consultar"
        if (respAlt != 's' or respAlt != 'S'):
            # A variavel "respAlt" recebe 's'
            respAlt = 's'
        # Repete a funcionalidade da opção
        while (respAlt == 's' or respAlt == 'S'):
            cons = input('\nDigite o nome do contato\n')
            if (cons in contatos):
                tipoCons = int(input('\nDeseja alterar o nome ou número?\n1 para o NOME\n2 para o NÚMERO\n'))
                if (tipoCons == 1):
                    nome = input('\nDigite o novo nome\n')
                    contatos[nome] = contatos.pop(cons)
                elif (tipoCons == 2):
                    num = input('\nDigite o novo número\n')
                    contatos[cons] = num
                else:
                    print('\nOpção inválida, por favor tente novamente')
                    tipoCons = int(input('\nDeseja alterar o nome ou número?\n1 para o NOME\n2 para o NÚMERO\n'))
            else:
                print('\nContato não encontrado!\n')

            # Aqui se pergunta se o usuário quer continuar
            respAlt = input('\nDeseja consultar outro contato? S para sim e N para não: ')

    # Caso selecione a opção de deletar (4) //Menu principal
    elif(opc == 4):
        print('\nDELETAR CONTATOS')
        # Se a resposta for negativa para "deletar"
        if (respDel != 's' or respDel != 'S'):
            # A variavel "respDel" recebe 's'
            respDel = 's'
        # Enquanto respDel valer 's' será executado
        while (respDel == 's' or respDel == 'S'):
            # Pergunta se o usuário deseja consultar pelo nome(1) ou pelo numero(2)
            tipoCons = int(input('\nComo deseja consultar?\n1 para consultar pelo NOME\n2 para consultar pelo NÚMERO\n'))
                
            if (tipoCons == 1):
                cons = input('\nDigite o nome do contato\n')
                print(contatos.pop(cons, 'Contato não encontrado'))
            elif (tipoCons == 2):
                cons = input('\nDigite o número do telefone\n')
                print(contatos.popitem(cons))

            # Aqui se pergunta se o usuário quer continuar
            respDel = input('\nDeseja consultar outro contato? S para sim e N para não: ')
                
    # Caso selecione a opção de consultar (5) //Menu principal
    elif (opc == 5):
        sorted(contatos.values())
        for item in contatos.keys():
            print ("Nome: {0} | Telefone: {1}" .format(item, contatos[item]))

   # Caso selecione a opção de sair (0)
    elif (opc == 0):
        # O contador do menu principal recebe +1 e encerra = 1
        cont+=1

    #  Caso tenha digitado errado //Menu principal        
    else:
        # Mensagem exibida caso tenha digitado errado
        print('\nERRO001: Opção inválida, favor tente novamente!')
            
# Mensagem de despedida ao encerrar o programa            
print('\n\nObrigada por utilizar nosso programa!')