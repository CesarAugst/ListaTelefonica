import pickle #modulo pickle

opc = 21
respAdc = 's'
respCons = 's'
respAlt = 's'
respDel = 's'
num = ''
importar = 21
contatos = {}
procura = ''

print('\nBEM VINDO A LISTA TELEFÔNICA 2019\n')

while (importar != 1 or importar != 2 or importar != 3):
    try:
        importar = int(input('\nDeseja importar ou criar uma agenda?\n1 para IMPORTAR\n2 para CRIAR UM NOVO\n3 para NÃO IMPORTAR NEM GRAVAR\n0 para SAIR\n'))
        if(importar == 1):
            nomeAgenda = input('\nQual é o nome do arquivo que deseja abrir? Obs: Caso o arquivo tenha extensão, não esqueça!\n')
            try:
                arq = open(nomeAgenda,'rb') # Abrir o arquivo para leitura - o "b" significa que o arquivo é binário
                contatos = pickle.load(arq) # Ler a stream a partir do arquivo e reconstroi o objeto original.
                arq.close() # Fechar o arquivo
                print('\nCONTATOS IMPORTADOS COM SUCESSO!')
                break
            except:
                print('\nAgenda não encontrada')
                importar = 21

        elif(importar == 2):
            nomeAgenda = input('\nQual será o nome da nova agenda?\n')
            arq = open(nomeAgenda,'wb') # Abrir o arquivo para gravação - o "b" significa que o arquivo é binário
            pickle.dump(contatos,arq) # Grava uma stream do objeto "contatos" para um novo arquivo
            arq.close() # fechar o arquivo
            break
        elif(importar == 3):
            print('\nCONTATOS NÃO IMPORTADOS!')
            break
        elif(importar == 0):
            break
        else:
            print('\nOpção inválida, favor tente novamente!')
    except:
        print('\nDigite somente números!')

# Repete o algoritmo por completo
while (opc != 0 and importar != 0):
    # Mostra o menu para o usuário   
    opc = int(input('\nDIGITE A OPÇÃO DESEJADA\n1 para CADASTRAR\n2 para CONSULTAR\n3 para ALTERAR\n4 para EXCLUIR\n5 para VISUALIZAR TODOS OS CONTATOS\n0 para SAIR\n'))

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
                if (procura != ''):
                    procura = ''
                for i in contatos:
                    if (contatos[i] == cons):
                        procura = i
                        break
                if (procura != ''):
                    print("Nome: {0} | Número: {1}" .format(procura, cons))
                else:
                    print('\nContato não encontrado!')
                    
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
            tipoCons = int(input('\nComo alterar deletar?\n1 para alterar pelo NOME\n2 para alterar pelo NÚMERO\n'))

            # Se a resposta for positiva para "nome"
            if (tipoCons == 1):
                cons = input('\nDigite o nome do contato\n')
                if (cons in contatos):
                    nome = cons
                    verifica = 1
                else:
                    print('\nContato não encontrado!')
            elif (tipoCons == 2):
                cons = input('\nDigite o número do telefone\n')
                if (procura != ''):
                    procura = ''
                for i in contatos:
                    if (contatos[i] == cons):
                        nome = i
                        break
                if (nome != ''):
                    verifica = 1
                else:
                    procura = ''
                    print('\nContato não encontrado!')

            if (verifica == 1):
                tipoCons = int(input('\nDeseja alterar o nome ou número?\n1 para o NOME\n2 para o NÚMERO\n'))
                if (tipoCons == 1):
                    nvNome = input('\nDigite o novo nome\n')
                    contatos[nvNome] = contatos.pop(nome)
                elif (tipoCons == 2):
                    num = input('\nDigite o novo número\n')
                    contatos[nome] = num
                else:
                    print('\nOpção inválida, por favor tente novamente')
                    tipoCons = int(input('\nDeseja alterar o nome ou número?\n1 para o NOME\n2 para o NÚMERO\n'))
            else:
                print('\nContato não encontrado!\n')

            # Aqui se pergunta se o usuário quer continuar
            
            respAlt = input('\nDeseja alterar outro contato? S para sim e N para não: ')

    # Caso selecione a opção de deletar (4) //Menu principal
    elif(opc == 4):
        print('\nDELETAR CONTATOS')
        # Se a resposta for negativa para "deletar"
        if (respDel != 's' or respDel != 'S'):
            # A variavel "respDel" recebe 's'
            respDel = 's'
        # Enquanto respDel valer 's' será executado
        while (respDel == 's' or respDel == 'S'):
            # Pergunta se o usuário deseja deletar pelo nome(1) ou pelo numero(2)
            tipoCons = int(input('\nComo deseja deletar?\n1 para deletar pelo NOME\n2 para deletar pelo NÚMERO\n'))
                
            if (tipoCons == 1):
                cons = input('\nDigite o nome do contato\n')
                print(contatos.pop(cons, 'Contato não encontrado'))
            elif (tipoCons == 2):
                cons = input('\nDigite o número do telefone\n')
                if (procura != ''):
                    procura = ''
                for i in contatos:
                    if (contatos[i] == cons):
                        procura = i
                        break
                if (procura != ''):
                    print(contatos.pop(procura, 'Contato não encontrado'))
                else:
                    print('\nContato não encontrado!')

            # Aqui se pergunta se o usuário quer continuar
            respDel = input('\nDeseja consultar outro contato? S para sim e N para não: ')
                
    # Caso selecione a opção de consultar (5) //Menu principal
    elif (opc == 5):
        tipoCons = int(input('\nComo deseja exibir?\n1 para exibir por ordem alfabética CRESCENTE(A-Z)\n2 para exibir por ordem alfabética DECRESCENTE(Z-A)\n3 para exibir em ordem CRESCENTE por número de telefone\n4 para exibir em ordem DECRESCENTE por número de telefone\n'))
        
        if (tipoCons == 1):
            # Exibe os contatos em ordem alfabética crescente (A-Z)
            for item in sorted(contatos.keys()):
                print ("Nome: {0} | Telefone: {1}" .format(item, contatos[item]))
        elif (tipoCons == 2):
            for item in sorted(contatos.keys(), reverse=True):
                print ("Nome: {0} | Telefone: {1}" .format(item, contatos[item]))
        elif (tipoCons == 3):
            for item in sorted(contatos, key = contatos.get):
                print ("Nome: {0} | Telefone: {1}" .format(item, contatos[item]))
        elif (tipoCons == 4):
            for item in sorted(contatos, key = contatos.get, reverse=True):
                print ("Nome: {0} | Telefone: {1}" .format(item, contatos[item]))
        
        input('\nENTER para continuar')

   # Caso selecione a opção de sair (0)
    elif (opc == 0):
        # Mensagem de despedida ao encerrar o programa   
        break
    #  Caso tenha digitado errado //Menu principal        
    else:
        # Mensagem exibida caso tenha digitado errado
        print('\nERRO001: Opção inválida, favor tente novamente!')   

    if (importar != 3):
            arq = open(nomeAgenda,'wb') #abrir o arquivo para gravação - o "b" significa que o arquivo é binário
            pickle.dump(contatos,arq) #Grava uma stream do objeto "contatos" para o arquivo.
            arq.close() #fechar o arquivo     

print('\nObrigada por utilizar nosso programa!')
