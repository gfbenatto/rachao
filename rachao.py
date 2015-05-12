#!/usr/bin/python


# quantidade de carne por pessoa
carne = 0.3

# quantidade de cerveja por pessoa
cerveja = 1.5

pessoas = raw_input("Digite o numero de pessoas: ")
if pessoas.isdigit() == False:
    print("Ops voce digitou algo que nao entendo, so sei fazer conta com numerais!!!!")
else:
    resultadocarne = float(pessoas)*carne
    print('A quantidade de carne necessaria resultadocarne e', resultadocarne, 'Kilos de carne')
    resultadocerveja = float(pessoas)*cerveja
    print('A quantidade de cerveja necessaria e', resultadocerveja, 'litros de cerveja')

