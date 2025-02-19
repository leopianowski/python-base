# 1.Faça um Programa que peça dois números e imprima o maior deles.
number1 = input('Insira o primeiro número: ')
number2 = input('Insira o segundo número: ')

if number1 > number2:
    print(f'O maior número foi o primeiro: {number1}')
elif number1 == number2:
    print('Os números inseridos são iguais')
else:
    print(f'O maior número foi o segundo: {number2}')

# 2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
if int(number1) >= 0:
    print(f'O número {number1} é positivo')
else:
    print(f'O número {number1} é negativo')

# 3.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
gender = input('Insira seu genêro, M para masculino ou F para feminino: ')

if gender == 'M' or  gender == 'm':
     print('Genêro Masculino')
elif gender == 'F' or gender == 'f':
    print('Genêro Feminino')
else:
    print('Genêro inválido')

# 4.Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Insira uma letra: ')
vogais = "aeiouAEIOU"

if letra.isalpha():
    if letra in vogais:
        print('A letrar é uma vogal')
    else:
        print('A letra é uma consoante')
else:
    print('Isso não é uma letra!')
"""
5.Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2)/2

if media >= 7 and media < 10:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
elif media == 10:
    print('Aprovado com Distinção')
else:
    print('Error')

# 6. Faça um Programa que leia três números e mostre o maior deles.
n1 = int(2)
n2 = int(3)
n3 = int(4)

if n1 > n2 and n1 > n3:
    print('N1 é maior')
elif n2 > n3 and n2 > n1:
    print('N2 é maior')
elif n3 > n1 and n3 > n2:
    print('N3 é maior')
else: 
    print('Não conclusivo')

"""
12.Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""
valor_hora = 200
horas_trabalhadas = 20
salario_bruto = valor_hora * horas_trabalhadas

#imposto de renda
irpercent = float(0)
if salario_bruto > 900 and salario_bruto <= 1500:
    irpercent = 0.05
elif salario_bruto > 1500 and salario_bruto <= 2500:
    irpercent = 0.10
elif salario_bruto > 2500:
    irpercent = 0.20

ir = irpercent * salario_bruto
inss = 0.10* salario_bruto
fgts = 0.11 * salario_bruto

print(f'Salário bruto (R${valor_hora:.2f} x {horas_trabalhadas}h: R${salario_bruto:.2f})')
print(f'(-) IR ({irpercent *100}%): R${ir:.2f}')
print(f'(-) INSS (10%): R${inss:.2f}')
print(f'FGTS (11%): R${fgts:.2f}')
print(f'Total de descontos: R${ir + inss}')
print(f'Salário Liquido: R${salario_bruto - (ir + inss)}') 