def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        palpite = int(input("Adivinhe um número entre 1 e 100: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            acertou = True
            print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")

if __name__ == "__main__":
    jogo_adivinhacao()