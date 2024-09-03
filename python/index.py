import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

print("\nO que você planeja fazer?")
print("1. Descobrir se é ímpar ou par")
print("2. Descobrir se passou ou não")
print("3. Obter várias notas")
escolha = int(input("Digite o número correspondente à sua escolha: "))

clear_screen()

if escolha == 1:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

elif escolha == 2:
    notas = []
    for i in range(4):
        nota = float(input(f"Por favor, digite a nota {i + 1}: "))
        notas.append(nota)
    media = sum(notas) / 4
    
    print(f"A média das notas é: {media:.2f}")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

elif escolha == 3:
    quantidade = int(input("Quantas notas vamos calcular? "))
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
        print("Me ajuda a te ajudar. escolhe 1 ou 2.")
        continue 
