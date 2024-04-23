from os import system
from random import randint 


def sorteio():
    voucher = randint(100,400)
    print(f'Seu Voucher: \033[32m{voucher}\033[m')


def cadastro():
    nome = input('Digite o seu nome: ')
    email = input('Digite o deu E-MAil: ')
    celular = input('Digite o seu Celular: ')
    curso = input('Digite o seu Curso: ')
    return{'nome': nome, 'email': email, 'celular': celular, 'curso': curso}




def inscritos(cadastrados):
    input('Lista de pessoas cadastradas! Aperte "ENTER" para ver a lista completa ')
    print('-'*70)
    for pessoas in cadastrados:
        sorteio()
        print(f"Nome: {pessoas['nome']}\nE-Mail: {pessoas['email']}\nCelular: {pessoas['celular']}\nCurso: {pessoas['curso']}\n")
    input('Aperte "ENTER" para voltar ao menu ') 


system('cls')
print('='*60)
print('Faça sua incrição para concorer as aulas \033[32mGRATIUTAS\033[m de \033[32mPYTHON\033[m ')
print('='*60)
enter = input('           Digite "ENTER" para o menu inicial.')






cadastrados = []




while True  :  
        
    system('cls')
    print('               ...................................')
    print('                               MENU')
    print('               ................................... ')
    print('''               1 - Nova inscrição
               2 - Visualizar inscrição
               0 - Encerrar''')
    opcao = (input('Digite a sua opção: '))


    if opcao == '1':
        system('cls')
        pessoas = cadastro()
        cadastrados.append(pessoas)
        print('Pessoa cadastrada com SUCESSO.')                  
    elif opcao == '2':
        system('cls')            
        if cadastrados:
            inscritos(cadastrados)
        else:
            input('Nenhum dado cadastrado! Aperte "Enter" pra voltar no menu')
    elif opcao == '0':
        break
    else:
        print('Escolha uma opção valida')




   


