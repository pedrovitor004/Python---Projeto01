#OBJETIVO DO PROJETO: CRIAR UM SISTEMA BACKEND EM PYTHON QUE TENHA DUAS VERTENTES (CLIENTE, FUNCIONÁRIOS)
#OBJETIVO DO PROJETO: PRATICAR LÓGICA DE PROGRAMAÇÃO EM PYTHON COM OBJETIVO DE DESENVOLVER APLICAÇÕES CORPORATIVAS
#OBJETIVO DO PROJETO: PRATICAR CONTEÚDOS ENSINADOS EM SALA DE AULA NA DISCIPLINA ALGORITMOS E LÓGICA DE PROGRAMAÇÃO

#LINGUAGEM UTILIZADA: PYTHON
from colorama import Fore, init
import emoji
#IMPORTAÇÃO DAS BIBLIOTECAS PYTHON COLORAMA E EMOJI
#ONJETIVO DAS BIBLIOTECAS: DÁ ESTÉTICA AO TERMINAL COM EMOJIS E CORES

sabores_escolhidos = [] #VARIÁVEIS E LISTAS DE CONTROLE
chave_funcionarios = ['admin'] #VARIÁVEL E LISTA COM UM INDICE PARA A CHAVE DE ACESSO
fichas_clientes = [] #VARIÁVEL DAS FICHAS DE ATENDIMENTO
pagamentos_clientes = [] #VARIÁVEL DO PAGAMENTO DOS CLIENTES
soma_total = 0
quanti_sabores = [] #QUANTIDADE DE SABORES 
quais_sabores = [] #QUAIS SABORES
           

init() #MÉTODO QUE INICIA A BIBLIOTECA COLORAMA

preco_produto = {
    'sorvete': 5.50,
    'milkshake': 13.00,
    'sundae': 6.50,
    'bebidas': 2.00}
sabores = {
    'sorvete': ["morango", "chocolate", "baunilha", "napolitano"],
    'milkshake': ["ovomaltine", "oreo", "paçoca", "menta"],
    'sundae': ["chocolate", "baunilha", "misto"]}

def entrada():
    while True:
        print(f'Seja bem-vindo a Sorvete Mania')
        verificacao_de_usuario = str(input(emoji.emojize(
            'Digite (001) para iniciar o sistema dos clientes :bust_in_silhouette: ou (002) para iniciar o dos '
            'funcionarios' ':bust_in_silhouette::\n')))
        if verificacao_de_usuario == '001':
            menu_pagamentos()
        elif verificacao_de_usuario == '002':
            funcionarios_login()
        else:
            print('Opção inválida\n')


def funcionarios_login():
    contador_tent = 3
    while contador_tent != 0:
        funcionario_chave = str(input(emoji.emojize("Chave de acesso:key:: "))).lower().strip()
        if funcionario_chave in chave_funcionarios:
            while True:
                funcionario_op = input(emoji.emojize("\nDigite uma das opções: \n"
                                                     "0 para voltar ao menu inicial \n"
                                                     "1 para abrir o cardápio :page_with_curl::\n"
                                                     "2 para abrir os pagamentos :money_with_wings::\n"
                                                     "3 para exibir o resumo do dia :door::\n")).strip()
                if funcionario_op == '0':
                    contador_tent = 0
                    break
                elif funcionario_op == '1':
                    menu_pagamentos()

                elif funcionario_op == '2':
                    tabela_pagamentos()

                elif funcionario_op == '3':
                    print(emoji.emojize(f'Número de pedidos do dia :bookmark_tabs:: {len(fichas_clientes)} '))
                    print(emoji.emojize(f'Caixa da loja:money_with_wings:: R${soma_total:.2f}\n'))
                else:
                    print('Digite uma opção válida')
        else:
            contador_tent -= 1
            print(f"Chave errada, restam {contador_tent} tentativas")


def menu_pagamentos():
    cores_cardapio = {
        "yellow": Fore.YELLOW,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "reset": Fore.RESET, }

    opcoes = [
        {'SORVETES': 'CHOCOLATE', 'PREÇO': 'R$ 5.50'},
        {'SORVETES': 'MORANGO', 'PREÇO': 'R$ 5.50'},
        {'SORVETES': 'BAUNILHA', 'PREÇO': 'R$ 5.50'},
        {'SORVETES': 'NAPOLITANO', 'PREÇO': 'R$ 5.50'},
        {'MILK': 'OVOMALTINE', 'PREÇO': 'R$ 13.00'},
        {'MILK': 'OREO', 'PREÇO': 'R$ 13.00'},
        {'MILK': 'PAÇOCA', 'PREÇO': 'R$ 13.00'},
        {'MILK': 'MENTA', 'PREÇO': 'R$ 13.00'},
        {'SUNDAE': 'CHOCOLATE', 'PREÇO': 'R$ 6.50'},
        {'SUNDAE': 'BAUNILHA', 'PREÇO': 'R$ 6.50'},
        {'SUNDAE': 'MISTO', 'PREÇO': 'R$ 6.50'},
        {'BEBIDAS': 'ÁGUA', 'PREÇO': 'R$ 2.00'}, ]
    print(emoji.emojize(f'{cores_cardapio["yellow"]}SORVETE MANIA :ice_cream:{cores_cardapio["reset"]}'))
    print(f'{cores_cardapio["magenta"]}\n{"." * 10}[CARDÁPIO]{"." * 10}{cores_cardapio["reset"]}')
    for item in opcoes:
        if 'SORVETES' in item:
            print(f'{cores_cardapio["cyan"]}\n[SORVETES:{cores_cardapio["reset"]}')
            print(f'{item["SORVETES"]:<20}{item["PREÇO"]}')
        elif 'MILK' in item:
            print(f'{cores_cardapio["cyan"]}\n[MILK SHAKE:{cores_cardapio["reset"]}')
            print(f'{item["MILK"]:<20}{item["PREÇO"]}')
        elif 'SUNDAE' in item:
            print(f'{cores_cardapio["cyan"]}\n[SUNDAE:{cores_cardapio["reset"]}')
            print(f'{item["SUNDAE"]:<20}{item["PREÇO"]}')
        elif 'BEBIDAS' in item:
            print(f'{cores_cardapio["cyan"]}\n[BEBIDAS:{cores_cardapio["reset"]}')
            print(f'{item["BEBIDAS"]:<20}{item["PREÇO"]}')
    pedidos_pagamentos()


def pedidos_pagamentos():
    global fichas_clientes, pagamentos_clientes, soma_total, sabores_escolhidos

    contador_ficha = len(fichas_clientes) + 1
    soma_pedido = 0

    while True:
        pedido = input("\nDigite o seu pedido (sorvete, milkshake, sundae, bebidas): ").lower().strip()
        if pedido in preco_produto:
            if pedido in sabores:
                while True:
                    if pedido == "sorvete":
                        sabores_escolha = input(
                            f"Escolha um ou mais sabores do {pedido} (separe por espaços): ").lower().strip()
                        for i in sabores_escolha.split(' '):
                            sabores_escolhidos.append(i)
                        if all(i in sabores[pedido] for i in sabores_escolhidos):
                            soma_pedido += preco_produto[pedido] * len(sabores_escolhidos)
                            print(f"Você escolheu {len(sabores_escolhidos)} sabores de {pedido}")
                            sabores_escolhidos = []
                            break
                        else:
                            print(f"Escolha sabores disponíveis para {pedido}")
                            sabores_escolhidos = []
                    elif pedido == "milkshake":
                        sabores_escolha = input(
                            f"Escolha um ou mais sabores do {pedido} (separe por espaços): ").lower().strip()
                        for i in sabores_escolha.split(' '):
                            sabores_escolhidos.append(i)
                        if all(i in sabores[pedido] for i in sabores_escolhidos):
                            soma_pedido += preco_produto[pedido] * len(sabores_escolhidos)
                            print(f"Você escolheu {len(sabores_escolhidos)} sabores de {pedido}")
                            sabores_escolhidos = []
                            break
                        else:
                            print(f"Escolha sabores disponíveis para {pedido}")
                            sabores_escolhidos = []
                    elif pedido == "sundae":
                        sabores_escolha = input(
                            f"Escolha um ou mais sabores do {pedido} (separe por espaços): ").lower().strip()
                        for i in sabores_escolha.split(' '):
                            sabores_escolhidos.append(i)
                        if all(i in sabores[pedido] for i in sabores_escolhidos):
                            soma_pedido += preco_produto[pedido] * len(sabores_escolhidos)
                            print(f"Você escolheu {len(sabores_escolhidos)} sabores de {pedido}")
                            sabores_escolhidos = []
                            break
                        else:
                            print(f"Escolha sabores disponíveis para {pedido}")
                            sabores_escolhidos = []
            else:
                soma_pedido += preco_produto[pedido]
        elif pedido == 'fp':
            break
        else:
            print("Escolha uma opção do cardápio")
            continue
        finalizar_continuar = input("\nDeseja finalizar o pedido (1) ou continuar (2)? ")
        if finalizar_continuar == '1':
            fichas_clientes.append(contador_ficha)
            pagamentos_clientes.append(f"{soma_pedido:.2f}")
            print(f"Valor total a pagar é R${soma_pedido:.2f}")
            soma_total += soma_pedido
            contador_ficha += 1
            soma_pedido = 0
        elif finalizar_continuar != '2':
            print("Dígito inválido, por favor refaça o(s) pedido(s)")
            soma_pedido = 0


def tabela_pagamentos():
    if len(fichas_clientes) > 0:
        print(f"\n{'Ficha:':<10}{'Total a pagar:'}")
        for i in range(len(fichas_clientes)):
            print(f"{fichas_clientes[i]:<10}R${pagamentos_clientes[i]:}")
        print(f"{'Total':<10}R${soma_total:.2f}")
    else:
        print("Nenhum pagamento registrado")


entrada()
