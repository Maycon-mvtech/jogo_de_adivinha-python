import random

def mostrar_boas_vindas():
    print("====================================")
    print("  Bem-vindo aso Jogo de Adivinhção")
    print("====================================")
    
def gerar_numero_secreto():
    return random.randint(1, 10)

print ("Tente adivinhar o número secreto!")
    
def pedir_chute():
    chute = int(input("Digite um número entre 1 e 10: "))
    return chute

def verificar_chute(chute, numero_secreto):
    if chute == numero_secreto:
        return "ACERTOU"
    elif chute > numero_secreto:
        return "MAIOR"
    else:
        return "MENOR"
    
def jogar ():
    mostrar_boas_vindas()
    numero_secreto = gerar_numero_secreto()
    tentativas = 0

    while True:
        chute = pedir_chute()
        tentativas += 1
        print(f"Você chutou {tentativas} vezes até agora")

        resultado = verificar_chute(chute, numero_secreto)

        if resultado == "ACERTOU":
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif resultado == "MAIOR":
            print("O número secreto é MENOR.")
        else:
            resultado == "MENOR"
            print(" O número secreto é MAIOR")

jogar()