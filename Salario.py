nome = input('Qual seu Nome :')
salario = int(input('Qual seu Salario :'))
aumento = (salario + (salario *10/100))
print ('Olá {} Ja que seu salario é {} então o seu aumento será {}'.format(nome, salario,aumento))