import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


quantidade = int(input("Quantas notas vamos calcular?: "))
notas = []

for i in range(quantidade):
    nota = float(input(f"Por favor, digite a nota {i + 1}: "))
    notas.append(nota)

clear_screen()

while True:
    print("\nO que você pretende fazer com as notas inseridas?")
    print("1. Somá-las")
    print("2. Calcular a média")

    escolha = int(input("Digite o número correspondente à sua escolha: "))

    if escolha == 1:
        soma = sum(notas)
        print(f"A soma das notas é: {soma:.2f}")
        break
    elif escolha == 2:
        media = sum(notas) / len(notas)
        print(f"A média das notas é: {media:.2f}")
        break
    else:

        print("Me ajuda a te ajudar! Por favor, escolha 1 ou 2.")
