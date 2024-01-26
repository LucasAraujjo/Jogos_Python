import adivinhacao

import forca


def iniciar_jogo():
    escolher_jogo()
    escolher_continuar()


def escolher_jogo():
    print("(1) para Adivinhação | (2) para Forca")
    resposta = int(input("Digite qual jogo quer jogar: "))

    if resposta == 1:
        adivinhacao.jogar()
    else:
        forca.jogar()


def escolher_continuar():
    print("---------------------")
    print("Quer continuar a jogar? (1)Sim | (2)Não")
    continuar = int(input("Digite sua opção: "))

    if (continuar == 1):
        escolher_jogo()
    else:
        fim_jogo()


def fim_jogo():
    print("---------------------")
    print("FIM DO JOGO!")
    print("---------------------")


iniciar_jogo()
