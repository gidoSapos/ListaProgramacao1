from codigos import isPositive, isEven, isLeapYear, \
isEven, higher_num, higherAndEquals, legalAge, \
isApproved, canRetire, caixaEletronico, typeTriangle


print('--'*50)
print('''Escreva um programa que leia um número e verifique se ele é positivo, negativo ou zero.''')
print(isPositive())

print('--'*50)
print('''Crie um programa que determine se um número é par ou ímpar.''')
print(isEven())

print('--'*50)
print('''Faça um programa que leia dois números e mostre o maior. Se forem iguais, informe que são iguais.''')
print(higher_num())

print('--'*50)
print('''Escreva um programa que verifique se um ano é bissexto.''')
print(isLeapYear())

print('--'*50)
print('''Faça um programa que leia dois números e
mostre o maior. Se forem iguais, informe que são iguais.''')
print(higherAndEquals())

print('--'*50)
print('''Desenvolva um algoritmo que leia a idade de uma
pessoa e informe se ela é menor de idade (menos de 18 anos), 
maior de idade (entre 18 e 64 anos) ou idosa (65 anos ou mais).''')
print(legalAge())

print('--'*50)
print('''Escreva um programa que calcule a média detrês notas 
e determine se o aluno está aprovado (média maior ou igual a 6), 
em recuperação (média entre 4 e 5.9) ou reprovado (média menor 
que 4).''')
print(isApproved())

print('--'*50)
print('''Crie um programa que leia o nome, idade e sexo de uma
pessoa e determine se ela pode se aposentar (homens a partir 
de 65 anos, mulheres a partir de 60 anos).''')
print(canRetire('giovanna' , 'female'))

print('--'*50)
print('''Desenvolva um algoritmo que simule um caixa 
eletrônico, onde o usuário informe o valor a ser sacado
e o programa exiba a quantidade de notas de 100, 50,
20, 10, 5 e 1 necessárias para o saque.''')
print(caixaEletronico())

print('--'*50)
print('''Escreva um programa que leia três lados de um 
triângulo e verifique se eles formam um triângulo válido. 
Se for válido, determine se é equilátero, isósceles ou 
escaleno.''')
print(typeTriangle())
