from map.module import *

while True:
    print(f'{"### - EMPRÉSTIMO DE REVISTAS - ###"}')
    print(f'{"(1) Cadastrar Revista"}')
    print(f'{"(2) Cadastrar Amigo"}')
    print(f'{"(3) Cadastrar Empréstimo"}')
    print(f'{"(4) Sair"}')
    opcao = validarInt('Opção: ')
    if opcao == 1:
        cadastrarRevista()
    elif opcao == 2:
        cadastrarAmigo()
    elif opcao == 3:
        cadastrarEmprestimo()
    elif opcao == 4:
        print('Saindo...')
        break
    else:
        print('Erro! Digite uma Opção entre 1 e 4.')