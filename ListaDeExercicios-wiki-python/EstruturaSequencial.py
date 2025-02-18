# 1.Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print('Alo mundo')

# 2.Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = input('Insira um número: ')
print(f'O número informado foi {numero}')

#3. Faça um Programa que peça dois números e imprima a soma.
numero1 = input('Insira o primeiro número: ')
numero2 = input('Insira o segundo número: ')
print(f'A somados dois número é {int(numero1) + int(numero2)}')

# 4.Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = input('Insira a primeira nota: ')
nota2 = input('Insira a segunda nota: ')
nota3 = input('Insira a terceira nota: ')
nota4 = input('Insira a quarta nota: ')
print(f'A média de suas notas é: {(int(nota1) + int(nota2) + int(nota3) + int(nota4))/4}')

# 5.Faça um Programa que converta metros para centímetros.
medida = input('Insira o número em metros que deseja converter para cm: ')
medida_convertida = int(medida) * 100
print(f'A medida em cm é: {medida_convertida}')

# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = input('Insira o valor do raio: ')
area = (float(raio)**2)
print(f'A área do seu círculo é: {area}π')

# 7.Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
tamanho_lado = input('Insira o tamanho do lado em cm: ')
area_quadrado = int(tamanho_lado) ** 2
print(f'A área do seu quadrado é {area_quadrado} e o dobro desta área é {tamanho_lado * 2}')

# 8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
remuneracao_hora = input('Insira quanto você ganha por hora (Ex:20.50):')
horas_trabalhadas = input('Insiera o número de horas trabalhadas: ')
salario = float(remuneracao_hora) * int(horas_trabalhadas)
print(f'O seu sálario mensal é: R${salario:.2f}') 

# 9.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
temperatura_fahrenheit = input('Insira a temperatura em F (apenas o valor): ')
temperatura_celsius = 5 * ((int(temperatura_fahrenheit)-32) / 9)
print(f'A temperatura em Celsius é: {temperatura_celsius}C')