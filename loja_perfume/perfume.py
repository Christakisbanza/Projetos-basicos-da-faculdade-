from os import system
from random import randint




def sorteio():
    voucher = randint(100,400)
    print(f'Seu Voucher: \033[32m{voucher}\033[m')




def cadastro():
    nome = input('Digite o seu Nome: ')
    email = input('Digite o deu E-MAil: ')
    celular = input('Digite o seu Celular: ')
    endereco = input('Digite o seu Endereço: ')
    input('\033[32mCadastro efetuado com Sucesso !\033[m')
    return{'nome': nome, 'email': email, 'celular': celular, 'endereco': endereco}




def Visualizar_cadastro(cadastrados):
    input('Lista de pessoas cadastradas! Aperte "ENTER" para ver a lista completa ')
    print('-'*70)
    for pessoas in cadastrados:
        sorteio()
        print(f"Nome: {pessoas['nome']}\nE-Mail: {pessoas['email']}\nCelular: {pessoas['celular']}\nEndereço: {pessoas['endereco']}\n")
    input('Aperte "ENTER" para voltar ao menu ')




def logo():
    print('          __|   _ \     __|')
    print('          _|    |  |   (   ')
    print('         ___|  ___/   \___|\n')




def escolha_M_F():
    print('\n           Escolha a categoria desejada')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('                                                      |')
    print(' 1 - Masculino        (2 - Feminino - Em breve...)    |')
    print('                                                      |')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
     
 
def escolha_masculino():
    escolha = input('\nDigite a opção e aperte "Enter" para proseguir  ')
    if escolha == '1':
        system('cls')
        logo()
        print('            -@@@@+@*                                               *%%@@%                                             ..-=-==..                              ')  
        print('            -@@@@=@#                                               *#%@@%                                             :=:=*#%%*                              ')
        print('            -@@@@-@*                                               *%@@@%                                             -+:+%%@@*                              ')
        print('            -@@@@-@*                                               *%@@@%                                             -+:+#%@@*                              ')
        print('         .=%@@@@@*#@@+                                             *%@@@%                                             :+-+#%@@+                              ')
        print('          +%@@@@@#%@@*                                           :@@@@@@@@:                                     ..-===++#++**#%+++===..                      ')
        print('          +%@@@@%##@%*                                          -@@%%@@@@@@@-                                   .:*####***##**####*#*:.                      ')
        print('          +%@@@@@##@@*                                         *@@%%%@@@@@@##*                                  .:*##**++++****#***#*:.                      ')
        print('          =%@@@@@@#@@*.                                        .%@%#%%%%@@@%*:                                  .:*#*****##++###**##*:.                      ')
        print('          =#@@@@@@#@@*                                         -@%#+####%%@@#=                                  .:*#*+***##*###***+**:.                      ')
        print('          =#@@@@@@#@%*.                                        =@@#**#####%%%-                                  .:*#*+*+****#*#+***#*:.                      ')
        print('          =#@@%@%@*%%+                                         +@@%#######%%%-                                  .:**+++*++*#*##****#*:.                      ')
        print('          :=++*###===:.                                        *@@%**######%%=                                  .:*#*****#***##****#*:.                      ')
        print('          ::====++=--:                                         #%##*+****###%+                                  .:*#**####*+####*###*:.                      ')
        print('   ID A1 \ SAUVAGE - Dior R$ 500,25                   ID A2 \   FAHRENHEIT - Dior R$ 850,73                ID A3 \ VERSACE - Eros R$ 1.000,58              \n')
        print('             ....                                                                                                                                            ')    
        print('             :--:                                                                                                                                            ')    
        print('            .-+*=.                                              .-++++++++=======.                                                                           ')    
        print('            .***#.                                              .+@@@@@@@@@@@@@@%:                                                                           ')    
        print('        .:=+%@@@@%+=:.                                          .*%%@@@@@@@@@@@@%:                                                                           ')  
        print('      .:-#@@@@@@@@@@%-:.                                        .#%%%%@@@@@@@@@@%:                                                                           ')  
        print('        .+%%%%@@@@@@*.                                          .#%%%%%%@@@@@@@@%:                                                                           ')  
        print('         -%@@@@@@@@%+                                           .#%%%%%%%%%%%@@%%:                                                                           ')  
        print('          *@@@@@@@@#                                                 -##*=---=-                                                                              ')  
        print('         .=%@@@@@@+.                                                 -##*=---=-                                                                              ')  
        print('         .:#@@@@@%:.                                       ..........-**+*====:..........                                                                    ')  
        print('        .=#%%%%%%%#=.                                      .:===-=++*+==::::--:-::---:::.                                                                    ')  
        print('       .*%%%#%%%%@%%*                                      .:+%####%%%%%%%%%@@%+++++==::.                                                                    ')  
        print('       -#%%%#@@@@@@%%*.                                    .:=#%%#***#####%%%%%*=+++=-:..                                                                    ')  
        print('     -%@@@@@@@@@@@@@@@@#.                                  .:=#%%@#########%%%%%+++--=:..                                                                    ')  
        print('         .:::------:                                       .:=*%%%@#########%%%@#+====...                                                                    ')  
        print('    ID A4 \ LE MAL    R$ 700,69                            .:+##%%%%%%%%%%%%%%%%@#+===...                                                                    ')
        print('                                                           .:+##%%#*@@@@@@@@@@@@#*###+:..                                                                    ')
        print('                                                           .:+%%%%%*%%%%@@@@@@@@#*##%*::.                                                                    ')
        print('                                                           .:+%%%%%*%%%%%%%@@@%@####%#-:.        ID A5 \ EDC Premium - R$ 3.854,95                           ')
        print('                                                           .:=%%%%%*%%%%%%%%%@%%######-:.                                                                    ')
        print('                                                           .:=%%%@%*@@@@@@@@@@@@###*##-:.                                                                    ')
        print('Atenção !!! Digitar somente um id por vez ! ')
        id = str(input('Digite o ID do produto desejado: ')).upper().strip()
        return{'id':id}
    elif escolha == '2':
        input('Produto disponível Em Breve ! Aperte "Enter" para voltar ao menu ')
    else:
        input('Error ! opção invalida.')


def carinho_compra(produtos_masculino):
    for compra in produtos_masculino:
        print(f"ID do produto : {compra['id']}")
        if compra['id'] == 'A1':
            print("Quantidade: 1")
            print('Nome do produto: SAUVAGE - Dior')
            print('Preço: R$ 500,25\n')
            input('\033[4;30;47mAperte "Enter" para confirmar o pedido\n\033[m')
        elif compra['id'] == 'A2':
            print("Quantidade: 1")
            print('Nome do produto: FAHRENHEIT - Dior')
            print('Preço: R$ 850,73\n ')
            input('\033[4;30;47mAperte "Enter" para confirmar o pedido\n\033[m')
        elif compra['id'] == 'A3':
            print("Quantidade: 1")
            print('Nome do produto: VERSACE - Eros')
            print('Preço: R$ 1.000,58\n ')
            input('\033[4;30;47mAperte "Enter" para confirmar o pedido\n\033[m')  
        elif compra['id'] == 'A4':
            print("Quantidade: 1")
            print('Nome do produto: LE MAL')
            print('Preço: R$ 700,69\n ')
            input('\033[4;30;47mAperte "Enter" para confirmar o pedido\n\033[m')  
        elif compra['id'] == 'A5':
            print("Quantidade: 1")
            print('Nome do produto: EDC Premium')
            print('Preço: R$ 3.854,95\n ')
            input('\033[4;30;47mAperte "Enter" para confirmar o pedido\n\033[m')
        elif compra['id'] == 'A1 A2':
            print("Quantidade: 2")
            print('Nome do produto:  SAUVAGE - Dior, FAHRENHEIT - Dior')
            print('Preço: R$ 1.350,98\n ')
            input('\033[4;30;47mAperte "Enter" para confirmar o pedido\n\033[m')
    input('\033[4;30;47mAperte "Enter" para volar ao menu e depois na opção "5" para finalizar a compra\033[m ')    
















def finalizar_compra():
    print("Dados pessoais:\n ")
    for pessoas in cadastrados:
        print(f"Nome: {pessoas['nome']}")
        print(f"E-mail: {pessoas['email']}\n")
    print('-'*43)
    for compra in produtos_masculino:
        print(f"\nID do Produto: {compra['id']} ")
        if compra['id'] == 'A1':
            print("Quantidade: 1")
            print('Nome do produto: SAUVAGE - Dior')
            print('Preço: R$ 500,25\n')
        elif compra['id'] == 'A2':
            print("Quantidade: 1")
            print('Nome do produto: FAHRENHEIT - Dior')
            print('Preço: R$ 850,73\n ')
        elif compra['id'] == 'A3':
            print("Quantidade: 1")
            print('Nome do produto: VERSACE - Eros')
            print('Preço: R$ 1.000,58\n')
        elif compra['id'] == 'A4':
            print("Quantidade: 1")
            print('Nome do produto: LE MAL')
            print('Preço: R$ 700,69\n ')
        elif compra['id'] == 'A5':
            print("Quantidade: 1")
            print('Nome do produto: EDC Premium')
            print('Preço: R$ 3.854,95\n ')
   




def total():
    soma = 0
    for compra in produtos_masculino:
        soma = soma + 1
    print(f'\nQuantidade total de items: {soma}\n ')
    pagamento = input('1 - Cartão de Credito           2 - Cartão de Debito ')
    if pagamento == '1' and soma >= 3:
        system('cls')
        print('     \033[32mPagamento realizado com sucesso\033[m\n')
        print(' ----------------------------------------')
        print('|              Nota Fiscal               |')
        print('|----------------------------------------|')
        print('|                                        |')
        print(f"| Pagador:  {pessoas['nome']}            ")
        print('|         -----------------------        |')
        print(f"| Quantidade de items: {soma}                 |")
        print('|         -----------------------        |')
        for compra in produtos_masculino:
            print(f"| ID do item: {compra['id']}                         | ")
        print('|         -----------------------        |')
        print('| \033[32mPagamento realizado no Debito\033[m          |')
        print('| Total : R$                             |')
        print('|                                        |')
        print('| Você ganhou 1 perfume grátis           |')
        print(' ----------------------------------------\n')
        input('Muito Obrigado pela preferência e volte sempre !')
    elif pagamento == '2' and soma >= 3:
        system('cls')
        print('     \033[32mPagamento realizado com sucesso\033[m\n')
        print(' ----------------------------------------')
        print('|              Nota Fiscal               |')
        print('|----------------------------------------|')
        print('|                                        |')
        print(f"| Pagador:  {pessoas['nome']}            ")
        print('|         -----------------------        |')
        print(f"| Quantidade de items: {soma}                 |")
        print('|         -----------------------        |')
        for compra in produtos_masculino:
            print(f"| ID do item: {compra['id']}                         | ")
        print('|         -----------------------        |')
        print('| \033[32mPagamento realizado no Debito\033[m          |')
        print('| Total : R$                             |')
        print('|                                        |')
        print('| Você ganhou 1 perfume grátis           |')
        print(' ----------------------------------------\n')
        input('Muito Obrigado pela preferência e volte sempre !')
    elif pagamento == '1':
        system('cls')
        print('     \033[32mPagamento realizado com sucesso\033[m\n')
        print(' ----------------------------------------')
        print('|              Nota Fiscal               |')
        print('|----------------------------------------|')
        print('|                                        |')
        print(f"| Pagador:  {pessoas['nome']}            ")
        print('|         -----------------------        |')
        print(f"| Quantidade de items: {soma}                 |")
        print('|         -----------------------        |')
        for compra in produtos_masculino:
            print(f"| ID do item: {compra['id']}                         | ")
        print('|         -----------------------        |')
        print('| \033[32mPagamento realizado no Credito\033[m         |')
        print('| Total : R$                             |')
        print(' ----------------------------------------\n')
        input('Muito Obrigado pela preferência e volte sempre !')
    elif pagamento == '2':
        system('cls')
        print('     \033[32mPagamento realizado com sucesso\033[m\n')
        print(' ----------------------------------------')
        print('|              Nota Fiscal               |')
        print('|----------------------------------------|')
        print('|                                        |')
        print(f"| Pagador:  {pessoas['nome']}            ")
        print('|         -----------------------        |')
        print(f"| Quantidade de items: {soma}                 |")
        print('|         -----------------------        |')
        for compra in produtos_masculino:
            print(f"| ID do item: {compra['id']}                         | ")
        print('|         -----------------------        |')
        print('| \033[32mPagamento realizado no Debito\033[m          |')
        print('| Total : R$                             |')
        print(' ----------------------------------------\n')
        input('Muito Obrigado pela preferência e volte sempre !')
 




















system('cls')
print('.-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-.')
print('|                            __|   _ \     __|                          |')
print('|                            _|    |  |   (                             |')
print('|                           ___|  ___/   \___|                          |')
print('|                                                                       |')
print('|                                                                       |')
print('!                                                                       !')
print(':                                                                       :')
print(':                                                                       :')
print('.                                                                       .')
print('    ____                                                                 ')
print('  /\  _`\                                                                ')
print('  \ \ \L\ \     __    ___ ___                                            ')
print('   \ \  _ <  / __ \/  __` __`\                                           ')
print('    \ \ \L\ \/\  __//\ \/\ \/\ \                                         ')
print('     \ \____/\ \____\ \_\ \_\ \_\                                        ')
print('      \/___/  \/____/\/_/\/_/\/_/                                        ')
print('.                                                                       .')
print(':                           __  __                  __                  :')
print(':                          /\ \/\ \  __            /\ \                 :')
print('!                          \ \ \ \ \/\_\    ___    \_\ \    ___         !')
print("|                           \ \ \ \ \/\ \ /' _ `\  /'_` \  / __`\       |")
print('|                            \ \ \_/ \ \ \/\ \/\ \/\ \L\ \/\ \L\ \      |')
print('|                             \ `\___/\ \_\ \_\ \_\ \___,_\ \____/      |')
print('|                              `\/__/  \/_/\/_/\/_/\/__,_ /\/___/       |')
print('|                                                                       |')
print('.=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=.')
enter = input('                   Aperte "ENTER" para iniciar  ')


cadastrados = []
produtos_masculino = []
estoque = ['SAUVAGE - Dior________',2, 'FAHRENHEIT - Dior_____',2 ,'VERSACE - Eros________',2 ,'LE MAL________________' ,2,'EDC Premium___________',2]






while True:  
    
    system('cls')
    logo()
    print('...................................')
    print('               MENU')
    print('...................................  ')
    print('        1 - Cadastre-se           .  ')
    print('        2 - Visualizar cadastros  .  ')   
    print('        3 - Fazer compras         .  ')    
    print('        4 - Carrinho de Compras   .  ')    
    print('        5 - Finalizar Compra      .  ')    
    print('        0 - Encerrar              .  ')    
    print('...................................  ')
    opcao = (input('Digite a sua opção: '))








    if opcao == '1':
        system('cls')
        logo()
        pessoas = cadastro()
        cadastrados.append(pessoas)
        print('Pessoa cadastrada com SUCESSO.')                  
    elif opcao == '2':
        system('cls')
        logo()          
        if cadastrados:
            Visualizar_cadastro(cadastrados)
        else:
            input('Nenhum dado cadastrado! Aperte "Enter" pra voltar no menu ')
    elif opcao == '3':
        system('cls')
        if cadastrados:
            logo()
            escolha_M_F()
            compra = escolha_masculino()
            produtos_masculino.append(compra)
        else:
            logo()
            input('Nunhum dado cadastado! Aperte "Enter" pra voltar no menu ')
    elif opcao == '4':
        system('cls')
        logo()
        if produtos_masculino:
            carinho_compra(produtos_masculino)
        else:
            input('Nunhum dado cadastado! Aperte "Enter" pra voltar no menu ')
    elif opcao == '5':
        system('cls')
        logo()
        if cadastrados and produtos_masculino:
            finalizar_compra()
            total()
        else:
            input('Cadastre se e adicione produtos no carrinho antes se finalizar a compra ')
    elif opcao == '0':
        break
    else:
        print('Escolha uma opção valida')












