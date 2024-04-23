from random import randint
from time import sleep
print('-'*37)
print('Tenta adivinhar o numero de 1 até 10 !!')
print('-'*37)
cout = 0
robo = randint(1, 10)
num = int(input('Digite o numero: '))
print('Processando....')
sleep(2)
if robo == num:
    print('Acertouu de primeira PARABENS, tava pensando no {} mesmo'.format(robo))

while robo != num:
    num2 = int(input(' - Tente novamente!! '))
    print('-'*40)
    cout = cout + 1
    if num2 == robo:
        print('Acertouu depois de {} tentativas, eu tava pensando no {} mesmo'.format(cout + 1, robo))
        robo = num
    else:
        if num2 < robo:
            print(' - È mais ')
        elif num2 > robo:
            print(' - È menos')
