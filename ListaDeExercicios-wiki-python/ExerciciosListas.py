#1.Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
vetor = [1,2,3,4,5]
print("Números na ordem normal:")
for i in vetor:
    print(i, end=" ")

#2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
print("\nNúmeros na ordem inversa:")
for i in vetor[::-1]:
    print(i, end=' ')

#3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas =[5,6,8,10]
notas_somadas = 0
print('\nAs notas são: ')
for i in notas:
    print(i, end=' ')
    notas_somadas += i

media = notas_somadas/len(notas)
print(f'\nE a média é: {media}')

#4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
vetor = [1,2,'t','q',5,'s',8,9,'d']
contador_letras = 0
contador_numeros = 0
for i in vetor:
    if str(i).isalpha():
        contador_letras += 1
    else:
        contador_numeros += 1

print(f'O número de letras é: {contador_letras}')

#5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
vetor_total = [1,2,3,4,5,6,7,8,9,10]
pares = []
impares = []

for i in vetor_total:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f'Todos: {vetor_total}\nPares: {pares}\nImpares: {impares}')

"""
14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

perguntas = ["Telefonou para a vítima? ",
            "Esteve no local do crime? ",
            "Mora perto da vítima? ",
            "Devia para a vítima? ",
            "Já trabalhou com a vítima? "]
respostas = []
contador = 0
print('Responda as perguntas a seguir com 1 para sim e 2 para não:')
for pergunta in perguntas:
    resposta = input(pergunta)
    if resposta not in ['1', '2']:
        print("Erro: Resposta inválida! Apenas '1' (sim) ou '2' (não) são permitidos.")
        break
    respostas.append(resposta)
    if resposta == '1':
        contador += 1
else:
    if contador <= 2:
        print('Você é suspeito!')
    elif 3 <= contador <= 4:
        print('Você é cúmplice!')
    elif contador == 5:
        print('Você é o assasino!')
    else:
        print('Você é inocente')        

print(respostas)