print("=== Verificador de idade ===")

while True:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    if idade >= 18:
        print(nome, "é maior de idade")
    else:
        print(nome, "é menor de idade")

    opcao = input("Deseja verificar outra pessoa? (s/n): ")

    if opcao != "s":
        print("Programa finalizado.")
        break
