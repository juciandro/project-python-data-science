import os

#listas: As listas são estruturas mutáveis
#lista = [1,’olá mundo’,True,9.7]
#restaurantes = []
#Dicionarios [{}]
restaurantes = [{'nome':'Bom Prato', 'categoria':'Regional', 'ativo':False},
                {'nome':'LaParrila', 'categoria':'Churrascaria', 'ativo':True},
                {'nome':'San Genaro', 'categoria':'Italiano', 'ativo':False}]

#tuplas: As tuplas são imutáveis
#tupla = (1,’olá mundo’,True,9.7)

def nome_app():
    print("""
        ⟆Ꭿᑲ𝖮ᖇ ᕮⲭᕈᖇ∈⟆⟆
    """)

def menu_app():
    print('1. Cadastrar Restaurantes')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair \n')

#functions
def encerrar_app():
    exibir_titulo('Encerrando programa ...')

def opcao_invalida():
    print('Opção invalida! \n')

    voltar_ao_menu()

def voltar_ao_menu():
    input('Digite uma tecla para voltar o menu principal ')
    main()

def exibir_titulo(titulo):
    os.system('cls')
    linha = '*' * len(titulo)
    print(linha)
    print(titulo)
    print(linha)
    print()

def cadastrar_restaurantes():

    '''Essa função é responsável por cadastrar um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante à lista de restaurantes

    '''

    exibir_titulo('Cadastrar novos Restaurantes')

    nome_restaurante = input('Informe o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Informe a categoria do restaurante {nome_restaurante}: ')
    #restaurantes.append(nome_restaurante)#(append) adiciona um valor a uma lista
    dados_restaurantes = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo':False}
    restaurantes.append(dados_restaurantes)#(append) adiciona um valor a um dicionario
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')

    voltar_ao_menu()
    

def listar_restaurantes():
    exibir_titulo('Lista de Restaurantes cadastrados')

    # para cada restaurante na lista restaurantes:
        # nome
    #print(f'{'Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurantes = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = f'Ativado' if restaurante['ativo'] else f'Desativado'
        #print(f'- {restaurante}')
        print(f'- {nome_restaurantes.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    

    print()
    voltar_ao_menu()

def atualizar_status_restaurante():
    exibir_titulo('Atualizar estado de Restaurantes cadastrados')

    nome_retaurante = input('Informe o nome do restaurante que deseja alterar o estado: ')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_retaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_retaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_retaurante} foi desativado com sucesso!'
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f'O restaurante {nome_retaurante} não foi encontrado!')

    print()
    voltar_ao_menu()


def escolher_opcao():

    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''

    try:
        opcao = int(input('Escolha uma opção: '))
        #opcao = int(opcao)

        #print(f'Sua opção escolida foi {opcao}.')

        if opcao == 1:
            #print('Cadastrar Restaurantes')
            cadastrar_restaurantes()
        elif opcao == 2:
            #print('Listar Restaurantes')
            listar_restaurantes()
        elif opcao == 3:
            #print('Ativar Restaurante')
            atualizar_status_restaurante()
        elif opcao == 4:
            encerrar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    nome_app()
    menu_app()
    escolher_opcao()

#define script como principal
if __name__ == '__main__':
    main()