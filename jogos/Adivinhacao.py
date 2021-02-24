import random

def jogar():

    mensagem_adivinhacao()

    numero_secreto = random. randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?", numero_secreto)
    print("(1) Fácil (2) Médio (3) Difícil")

    nível = int (input("Defina o nível: "))


    if(nível == 1):
        total_de_tentativas = 20
    elif(nível == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}". format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Voce digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Voce acertou e fez {} pontos!". format(pontos_finais))
            break
        else:
            if(maior):
                print("O seu chute foi maior que o número secreto." )
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Voce fez {} pontos." . format(numero_secreto, pontos_finais))
            elif(menor):
                print("O seu chute foi menor que o número secreto." )
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Voce fez {} pontos." . format(numero_secreto, pontos_finais))
            pontos_perdidos = abs(numero_secreto - chute)/3 #40-20=20
            pontos_finais = pontos - pontos_perdidos

        rodada = rodada + 1




    print("Fim de jogo.")


if(__name__ == "__main__"):
    jogar()


def mensagem_adivinhacao()
    print ("**********************************")
    print("Bem vindo ao jogo de Adivinhacao!")
    print ("**********************************")