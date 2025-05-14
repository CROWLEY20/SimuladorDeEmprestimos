import time

nome = input('Olá, bem vindo ao programa de empréstimos do banco JpNews Bank!\nQual é seu nome?')

valor_casa = float(input("Para começarmos, qual o valor da casa?"))
salario = float(input("Qual o valor do seu salário?"))
ano = int(input("Em quantos anos deseja pagar a casa?"))

mes = ano*12

prest = valor_casa/mes

limite = salario * 0.30

exced = prest - limite

print('Calculando...')

time.sleep(1.5)

if prest > limite:
    excedente = prest - limite
    print (f'O valor da sua prestação excedeu o limite de 30% do seu salário.')
    print (f'Infelizmente não será possível fazer o empréstimo.')
    print (f'O valor excedente foi de R${excedente:.2f}.')
else:
    print(f'Você foi aprovado! o valor da parcela do seu empréstimo é de {prest}.')