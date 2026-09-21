def teste(x, y):
    print(f'A soma de {x} e {y} é {x + y}')

teste(2, 3)

def soma(x, y, z):
    # Definição
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')

def soma2(x, y, z):
    return x + y + z

print(soma2(1, 2, 3))

def soma3(*args):
    return sum(args)

print(soma3(1, 2, 3, 4, 5))

# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


resultado = multiplica(1, 2, 3, 4, 5)
print(resultado)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'par'
    return 'ímpar'


print(par_ou_impar(10))
print(par_ou_impar(7))