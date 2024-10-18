import random

def usuario():
    while True:
        escolha = input("Escolha pedra, papel ou tesoura: ").lower()
        if escolha in ['pedra', 'papel', 'tesoura']:
            return escolha
        print("Opção inválida! Tente novamente.")

def maquina():
    return random.choice(['pedra', 'papel', 'tesoura'])

def partida(jogador, computador):
    if jogador == computador:
        return "Empate!"
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        return "Você ganhou!"
    else:
        return "Computador ganhou!"

def main():
    jogador = usuario()
    computador = maquina()
    print(f"Você escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")
    resultado = partida(jogador, computador)
    print(resultado)

if __name__ == "__main__":
    main()
