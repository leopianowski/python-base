import re 
import sys

cpf = re.sub(
    r'[^0-9]',
    '',
    input('Dígite o CPF: ')) 

# verificador de dados iguais (ex: 11111111111)
verificador = cpf == cpf [0]  * len(cpf)

if verificador:
    print('Você enviou dados iguais!')
    sys.exit()

# gerador do primeiro dígito
nove_digitos = cpf[:9]

soma1 = 0  
y = 10
primeiro_digito = 0

for i in nove_digitos:
    soma1 += int(i) * y  
    y -= 1  
digito = soma1 * 10
if digito % 11 > 9:
    primeiro_digito = 0
else:
    primeiro_digito = digito % 11
print(f'O primeiro dígito é {primeiro_digito}')

# gerador do segundo dígito
dez_digitos = nove_digitos + str(primeiro_digito)
soma2 = 0  
y = 11
segundo_digito = 0

for z in dez_digitos:
    soma2 += int(z) * y  
    y -= 1  
digito2 = soma2 * 10
if digito2 % 11 > 9:
    segundo_digito = 0
else:
    segundo_digito = digito2 % 11
print(f'O segundo dígito é {segundo_digito}')

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf_gerado == cpf:
    print(f'{cpf} é válido')
else:
    print('CPF inválido!')