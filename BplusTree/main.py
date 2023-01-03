from bPlusTree import *

tree = bPlusTree(128)

while True:
    print('#'*15,' ÁRVORE B+ ', '#'*15)
    print('Escolha uma das opções abaixo:')
    print('1 - Inserir valor')
    print('2 - Remover valor')
    print('3 - Procurar valor')
    print('4 - Iniciar testes')
    print('5 - Sair')
    try:
        chat = int(input('Digite aqui: '))
        if chat == 1:
            tree.insert(int(input("Digite um inteiro: ")))
            tree.print()

        elif chat == 2:
            tree.remove(int(input("Digite um inteiro: ")))
            tree.print()

        elif chat == 3:
            tree.search(int(input("Digite um inteiro: ")))

        elif chat == 4:
            print("Iniciando testes...")
            for i in range(1,100):
                tree.insert(i)

            tree.print()

        elif chat == 5:
            print('Saindo do programa...')
            tree.insert(chat)
            break

        else:
            int('ERROR')
    except:
        print('ERRO: Formatação ou operação inválida!!!')
        tree.remove(int(input("Digite um inteiro: ")))
