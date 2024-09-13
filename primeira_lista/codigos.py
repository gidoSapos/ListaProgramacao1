def isPositive() -> bool:
    while True:
        try:
            numero = float(input('Insira o número que você quer verificar se é positivo, negativo ou nulo: '))
            return numero > 0 if numero != 0 else None
        except ValueError:
                print('Não pode ser outra coisa além de um número.')

def isEven() -> bool:
    while True:
        try:
            num = float(input('Insira um número para verificar se é par ou impar: '))
            return True if num % 2 ==0 else False
        except ValueError:
            print('É só númeROOOOOOOOOOOOOOOOOOOOOOOOOO imbecil')

def higher_num() -> float:
    while True:
        try:
            segmento_numerico = [float(num) for num in input('Insira os números que queira verificar o maior. \n(na mesma linha separado por virgula)\nDigite:').split(',')]
            return f'O maior número é: {max(segmento_numerico)}'
        except ValueError: 
            print('nomero!!!!!!!')


def isLeapYear() -> bool:
    while True:
        try:
            ano = int(input('QUal o ano que vc quer checar palhaço????: '))
            return True if ano % 4 == 0 or ano % 100 == 0 or ano % 400 == 0 else False
        except ValueError:
            print('É um ano ou uma pessoa, vagabundo? Digita só números')


def higherAndEquals() -> tuple: 
    while True:
        try:
            lista_num = input('Por favor insira os números\n(na mesma linha separado por virgula)\nDigite:\n').split(',')
            numero = [float(num) for num in lista_num]
            maior_num = max(numero)
            num_duplicados = [num for num in numero if numero.count(num) > 1]
            return f'Os numeros duplicados são: {num_duplicados}\n O maior número é: {maior_num}'
        except ValueError:
            print('SOMENTE NUMEROSOSOOSOSOSOSOSOSOS....')


def legalAge() -> str:
    while True:
        try:
            idade = int(input('Insira anos: '))
            return 'Lixo humano e criança' if idade < 18 else 'Cometa um crime e "visite" Carandiru' if idade < 64 else 'Se enterra, peido velho enlatado'
        except ValueError:
            print('DONT insert letters, airhead.')


def isApproved() -> str:
    while True:
        try:
            notas = [float(nota) for nota in input('Insira as notas, fracassado (separado por virgula): ').split(',')]
            media = sum(notas)/len(notas)
            return 'Aprovado' if media >= 6 else 'melhore' if media <= 5.9 and media >= 4 else 'vc n tem salvação. smt'
        except ValueError:
            print('Só numeros baleia cachalote')


def canRetire(nome : str, sexo : str) -> str:
    while True:
        try:
            idade = int(input('Insira sua idade, por favor: '))
            if 'F' in sexo.upper()[0]:
                if idade > 60:
                     return f'Mrs.{nome.capitalize()}, can retire.' 
                else: 
                    return f'You still have to work for a few years before retiring Mrs.{nome.capitalize()}.'
            if 'M' in sexo.upper()[0]:
                if idade > 60:
                    return f'Mr.{nome.capitalize()}, can retire.'
                else: 
                    return f'You have a few years before retirement Mr.{nome.capitalize()}.'
            else:
                return 'Please insert a valid sex option'
        except ValueError:
            print('APENAS NUMEROS INTEIROOOOOOOOOOOOOOOOOOOOOOOOOOOOOS')


def caixaEletronico() -> int:
    while True:
        try:
            valor_saque = float(input('QUANTOS REALS VC QUER ASSALTAR DO BANCO::: '))
            notas = [100, 50, 20, 10, 5, 1]
            quantidade_notas = [0, 0, 0, 0, 0, 0]

            for i, nota in enumerate(notas):
                quantidade_notas[i] = valor_saque // nota
                valor_saque %= nota
            print("Quantidade de notas necessárias:")
            print(f"Notas de R$ 100: {quantidade_notas[0]}")
            print(f"Notas de R$ 50: {quantidade_notas[1]}")
            print(f"Notas de R$ 20: {quantidade_notas[2]}")
            print(f"Notas de R$ 10: {quantidade_notas[3]}")
            print(f"Notas de R$ 5: {quantidade_notas[4]}")
            print(f"Notas de R$ 1: {quantidade_notas[5]}")
            return '\nProcesso concluido'
        except:
            if valor_saque < 0:
                print('vc que quer assaltar o banco, não o contrario')
                

def typeTriangle() -> str:
    while True:
        try:

            lado1 = float(input('Por favor insira o valor do primeiro lado do triangulo: '))
            lado2 = float(input('Por favor insira o valor do segundo lado: '))
            lado3 = float(input('Agora o terceiro: '))

            if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
                print('Os lados DEVEM ser positivos.')
                continue

            lados = [lado1, lado2, lado3]
            lados.sort()
            if lados[1] + lados[0] > max(lados):
                return 'Its an scalene triangle' if lado1 != lado2 != lado3 else 'Its an equilateral triangle' if lado1 == lado2 == lado3 else 'Its an isosceles triangle'
            
        except ValueError:
            print('Insira um valor valido')

    
