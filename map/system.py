from module import *
from time import sleep

while True:
    print(f'{"-------------------------------"}')
    print(f'{"### EMPRÉSTIMO DE REVISTAS  ###"}')
    print(f'{"-------------------------------"}')
    print(f'{"(1) Cadastrar Revista"}')
    print(f'{"(2) Cadastrar Amigo"}')
    print(f'{"(3) Cadastrar Empréstimo"}')
    print(f'{"(4) Ver Lista de Revistas"}')
    print(f'{"(5) Ver Lista de Amigos"}')
    print(f'{"(6) Ver Lista de Empréstimos"}')
    print(f'{"(7) Sair"}')
    print(f'{"-------------------------------"}')
    opcao = validarInt('Opção: ')

    if opcao == 1:
        cadastrarRevista()
    elif opcao == 2:
        cadastrarAmigo()
        pause()
        continue
    elif opcao == 3:
        if len(listaRevistas) == 0 or len(listaAmigos) == 0:
            if len(listaRevistas) == 0:
                print('\033[0;31mErro! Não temos Nenhuma revista Cadastrada...\033[m')
                print('\033[0;33mCadastre uma Revista primeiro.\033[m')
                pause()
            else:
                print('\033[0;31mErro! Não temos Nenhum amigo Cadastrado...\033[m')
                print('\033[0;33mCadastre um Amigo primeiro.\033[m')
                pause()
        else:
            cadastrarEmprestimo()
    elif opcao == 4:
        if len(listaRevistas) == 0:
            print('\033[0;33mA Lista de Revistas está Vazia!\033[m')
            pause()
            continue
        else:
            imprimirListaRevistas()
            pause()
            continue
    elif opcao == 5:
        if len(listaAmigos) == 0:
            print('\033[0;33mA Lista de Amigos está Vazia!\033[m')
        else:
            imprimirListaAmigos()
            pause()
            continue
    elif opcao == 6:
        if len(listaEmprestimo) == 0:
            print('\033[0;33mA Lista de Empréstimos está Vazia!\033[m')
        else:
            imprimirListaEmprestimos()
            pause()
            continue
    elif opcao == 7:
        print('Saindo...')
        sleep(1)
        break
    else:
        print('\033[0;31mErro! Digite uma Opção Válida...\033[m\n'
              '\033[0;33mExemplo: Opção: de 1 até 7\033[m')
    pause()

