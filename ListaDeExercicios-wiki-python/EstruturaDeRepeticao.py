#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    try:
        nota = float(input("Digite uma nota entre 0 e 10: "))
        if 0 <= nota <= 10:
            print(f"Nota válida: {nota}")
            break  # Sai do loop se a nota for válida
        else:
            print("❌ Valor inválido! Digite uma nota entre 0 e 10.")
    except ValueError:
        print("⚠️ Entrada inválida! Por favor, digite um número.")
#2.Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if senha == usuario:
        print("❌ Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")
    else:
        print("✅ Cadastro realizado com sucesso!")
        break  # Sai do loop se a senha for diferente do nome
