from emoji import emojize 
from os import system 
system('cls')
def inicio1():
    reiniciar = input('\033[31m    "ERROR"\033[m Voce digitou um numero invalido. Aperta "Enter" para Jogar novamente.')
    system('cls')
    a = 1        
a = 1
while a != 0:
    print('\033[33m=-\033[m'*24)
    print('        Bem Vindo ao Jogo do Hotel ')
    print('\033[33m=-\033[m'*24)
    print('''-> Para poder se hospedar em nosso hotel        \033[33m|\033[m \ntem algumas regras a serem respeitadas          \033[33m|\033[m
    * - O Rato não pode ficar ao lado do gato   \033[33m|\033[m
    * - O Cão não pode ficar ao lado do osso    \033[33m|\033[m
    * - O Gato não pode ficar ao lado do cão    \033[33m|\033[m
    * - O Queijo não pode ficar ao lado do rato \033[33m|\033[m''')          
    print('\033[33m-\033[m'*47)
    enter = input('Aperte "Enter" para continuar: ')
    system('cls')
    print('            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('                            Fase 1 ')
    print('            =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('''            - Nessa primeira fase devem se alocar :
            Rato e Gato
            \033[4;30;46mEscolha entre "1" - "2"\033[m
            1 - Hospedar o Gato no quarto de cima e o Rato no de baixo.
            2 - Hospedar o Rato no quarto de cima e o Gato no de baixo.
            - Levando em consideração que já tem um "GATO" e um "RATO" alocados e
            os quartos com "x" já estão ocupados.
            --> Aperte "Enter" para sair''')
    print('''             ________________________________
            |  X   |    X   |        |   🐈  |
            |______|________|________|_______|
            | 🐁   |        |    X   |   X   |
            |______|________|________|_______|
            ''')
    fase1 = int(input('Digite sua resposta, dps aperte "Enter" para Confirmar: '))
    if fase1 == 2:
        system('cls')
        print('--- Voce \033[31mperdeu\033[m, não pode deixar o Rato perto de Gato! --- ')
        print('''             ________________________________
            |  X   |    X   |   🐁   |   🐈  |
            |______|________|________|_______|
            | 🐁   |   🐈   |    X   |   X   |
            |______|________|________|_______|
            ''')
        inicio = int(input('    Digite "1" e dps aperte "Enter" para jogar novamente: '))
        if inicio == 1:
            system('cls')
            a = 1
        else:
            inicio1()
    elif fase1 == 1:
        system('cls')
        print('''             ________________________________
            |  X   |    X   |   🐈   |   🐈  |
            |______|________|________|_______|
            |  🐁  |   🐁   |    X   |   X   |
            |______|________|________|_______|\n
              \033[32mCertinho! Você passou de fase.\033[m
            \n --> Aperte "Enter" para sair''')
        fase2 = int(input('Digite o numero "2" e dps aperte "Enter" pra seguir na fase 02: '))
        if fase2 != 2:
            inicio1()
        elif fase2 == 2:
            system('cls')
            print('                  =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print('                                 Fase 2')
            print('                  =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print('''                - Nessa segunda fase devem se alocar:
                  Cão, Cão e Osso
                  \033[4;30;46mEscolha entre "1" - "2" - "3"\033[m
                  3 - Hospedar nos quartos: Cão em cima - Osso em baixo esquerda - Cão em baixo direita.
                  2 - Hospedar nos quartos: Cão em cima - Osso em baixo direita - Cão em baixo esquerda.
                  1 - Hospedar nos quartos: Cão em baixo - Cão em baixo - Osso em cima.
                  - Levando em consideração que já tem um "Cão" alocado e
                  os quartos com "x" já estão ocupados.
                  --> Aperte "Enter" para sair''')
            print('''                 ________________________________
                |      |    X   |    x   |   x   |
                |______|________|________|_______|
                |   x  |    🐶  |        |       |
                |______|________|________|_______|
                ''')
            fase2 = int(input('Digite a sua resposta, dps aperte "Enter" para Confirmar: '))
            if fase2 == 3:
                system('cls')
                print(' --- Voce \033[31mperdeu\033[m, não pode deixar o Cão perto do Osso ')
                print('''                 ________________________________
                |  🐶  |    X   |    x   |   x   |
                |______|________|________|_______|
                |   x  |    🐶  |   🦴   |  🐶   |
                |______|________|________|_______|
                ''')
                inicio = int(input('     Digite o numero "1" e dps aperte "Enter" para jogar novamente: '))
                if inicio == 1:
                    system('cls')
                    a = 1
                else:
                    inicio1()
            elif fase2 == 2:
                system('cls')
                print(' --- Voce \033[31mperdeu\033[m, não pode deixar o Osso perto do Cão.')
                print('''                 ________________________________
                |  🐶  |    X   |    x   |   x   |
                |______|________|________|_______|
                |   x  |    🐶  |   🐶   |   🦴  |
                |______|________|________|_______|
                ''')
                inicio = int(input('     Digite o numero "1", dps aperte "Enter" para jogar novamnete: '))
                if inicio == 1:
                    system('cls')
                    a = 1
                else:
                   inicio1()
            elif fase2 == 1:
                system('cls')
                print('''                     ________________________________
                    |  🦴  |    X   |    x   |   x   |
                    |______|________|________|_______|
                    |   x  |   🐶   |    🐶  |   🐶  |
                    |______|________|________|_______|\n
                       \033[32mCertinho! Você passou de fase.\033[m
                    \n --> Aperte "Enter" para sair''')
                fase3 = int(input('Digite "3" e dps aperte "Enter" para fase 3: '))
                if fase3 != 3:
                    inicio1()
                elif fase3 == 3:
                    system('cls')
                    print('                        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                    print('                                       Fase 3')
                    print('                        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                    print('''                      - Nessa terceira fase devem se alocar:
                        Gato, Rato e Osso
                        \033[4;30;46mEscolha entre "1" - "2" - "3"\033[m
                        1 - Hospedar nos quartos: Osso em cima - Gato em baixo esquerda - Rato em baixo direita.
                        2 - Hospedar nos quartos: Rato em cima - Gato em baixo direita - Osso em baixo direita.
                        3 - Hospedar nos quartos: Osso em baixo esquerda -Rato em baixo esquerda - Gato em cima.
                        - Levando em consideração que já tem um "Gato" alocado e
                        os quartos com "x" já estão ocupados.
                        --> Aperte "Enter" para sair''')
                    print('''                         ________________________________
                        |      |    X   |    x   |   x   |
                        |______|________|________|_______|
                        |      |    🐈  |        |   x   |
                        |______|________|________|_______|
                        ''')
                    fase3 = int(input('Digite a sua resposta, dps aperte "Enter" para Confirmar: '))
                    if fase3 == 1:
                        system('cls')
                        print('Voce \033[31mperdeu\033[m, nao pode deixar o Rato perto do Gato')
                        print('''                         ________________________________
                        |  🦴  |    X   |    x   |   x   |
                        |______|________|________|_______|
                        |  🐈  |    🐈  |   🐁   |   x   |
                        |______|________|________|_______|
                        ''')
                        inicio = int(input('     Digite o numero "1" e dps aperte "Enter" para voltar no inicio: '))
                        if inicio == 1:
                            system('cls')
                            a = 1
                        else:
                            inicio1()
                    elif fase3 == 2:
                        system('cls')
                        print('Voce \033[31mperdeu\033[m, nao pode deixar o Rato perto do Gato')
                        print('''                         ________________________________
                        |  🐁  |    X   |    x   |   x   |
                        |______|________|________|_______|
                        |  🐈  |    🐈  |   🦴   |   x   |
                        |______|________|________|_______|
                        ''')
                        inicio = int(input('     Digite o numero "1", dps aperte "Enter" para voltar no inicio: '))
                        if inicio == 1:
                            system('cls')
                            a = 1 
                        else:
                            inicio1()
                    elif fase3 == 3:
                        system('cls')
                        print('''                             ________________________________
                            |  🐁  |    X   |    x   |   x   |
                            |______|________|________|_______|
                            |  🦴  |    🐈  |   🐈   |   x   |
                            |______|________|________|_______|
                            ''')
                        print('                  \033[32mParabens Você conseguui passar na quarta e ultima fase!!\033[m \n --> Aperte "Enter" para sair ')
                        fase4 = int(input('Digite o numero "4" e dps aperte "Enter" para a fase 04: '))
                        if fase4 != 4:
                           inicio1()
                        elif fase4 == 4:
                            system('cls')
                            print('                                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                            print('                                              Fase 4')
                            print('                                =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                            print('''                              - Nessa quarta fase devem se alocar:
                                Queijo, Queijo e Osso
                                \033[4;30;46mEscolha entre "1" - "2" - "3"\033[m
                                1 - Hospedar nos quartos: Queijo em cima (Direita) - Osso em cima (Esquerda) - Queijo em cima (Meio)
                                2 - Hospedar nos quartos: Osso em cima (Meio) - Queijo em cima (Direita) - Queijo em cima (Esquerda)
                                3 - Hospedar nos quartos: Queijo em cima (Esquerda) - Queijo em cima (Direita) - Osso em cima (Direita)
                                - Levando em consideração que já tem um "Cão" alocado e
                                os quartos com "x" já estão ocupados.
                                --> Aperte "Enter" para sair''')
                            print('''                                 ________________________________
                                |      |        |        |   x   |
                                |______|________|________|_______|
                                |   x  |   🐁   |    x   |   x   |
                                |______|________|________|_______|
                                ''')
                            fase4 = int(input('Digite a sua resposta, dps aperte "Enter" para Confirmar: '))
                            if fase4 == 2:
                                system('cls')
                                print('''                                     __________________________________
                                    |   🧀   |   🦴   |  🧀    |   x   |
                                    |________|________|________|_______|
                                    |    x   |   🐁   |    x   |   x   |
                                    |________|________|________|_______|
                                    ''')
                                inicio = input('                                       \033[32mParabens Você "ZEROU O JOGO"\033[m. Aperte "Enter" para Jogar novamnete')
                                system('cls')
                                a = 1
                            elif fase4 == 1:
                                system('cls')
                                print('                             --- Voce \033[31mperdeu\033[m, nao pode deixar o Rato perto do Queijo')
                                print('''                                     __________________________________
                                    |   🦴   |   🧀   |  🧀    |   x   |
                                    |________|________|________|_______|
                                    |    x   |   🐁   |    x   |   x   |
                                    |________|________|________|_______|
                                    ''')
                                inicio2 = int(input('     Digite o numero "1" e dps aperte "Enter" para voltar no inicio: '))
                                if inicio2 == 1:
                                    system('cls')
                                    a = 1
                                else:
                                    inicio1()
                            elif fase4 == 3:
                                system('cls')
                                print('                             --- Voce \033[31mperdeu\033[m, nao pode deixar o Queijo perto do Gato')
                                print('''                                     __________________________________
                                    |   🧀   |   🧀   |  🦴    |   x   |
                                    |________|________|________|_______|
                                    |    x   |   🐁   |    x   |   x   |
                                    |________|________|________|_______|
                                    ''')
                                inicio = int(input('     Digite o numero "1" e dps aperte "Enter" para volatr no inicio: '))
                                if inicio == 1:
                                    system('cls')
                                    a = 1
                                else:
                                   inicio1()
                            else:
                                system('cls')
                                inicio1()








                     
                    else:
                       inicio1()
            else:
                inicio1()
    else:
       inicio1()





