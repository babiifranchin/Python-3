import Forca
import Adivinhacao

def escolhe_jogo():

    mensagem_jogos()

    print("(1) Forca (2) Adivinhacao")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando Forca.")
        Forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhacao.")
        Adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()


def mensagem_jogos
    print("**********************************")
    print("********Escolha seu jogo!**********")
    print("**********************************")