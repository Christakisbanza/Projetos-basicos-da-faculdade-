media = count = soma = m = me = 0
per = 'S'
while 'S' in per:
    n1 = int(input('Digite um numero: '))
    per = str(input('Quer continuar? [S/N]')).upper()
    count = count + 1
    soma = soma + n1
    if count == 1:
        m = n1
        me = n1
    else:
        if n1 > m:
            m = n1
        elif n1 < me:
            me = n1
media = soma / count
print(f'Voce digitou {count} numeros \nA media dos numeros é de {media:.2f}, o maior é de {m} e o menor é de {me}')
