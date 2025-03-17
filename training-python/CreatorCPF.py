import random

nove_digitos = ''

for i in range (9):
    nove_digitos += str(random.randint(0, 9))

# gerador do primeiro dígito
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


cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

print(f'O CPF gerado é: {cpf_gerado}')
