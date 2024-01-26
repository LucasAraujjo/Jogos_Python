import random


def jogar():
    print("---------------------")
    print("Bem vindo ao jogo de forca")
    print("---------------------")

    # abre meu arquivo
    arquivo = open("palavras.txt", "r")

    # cria uma lista
    palavras = []

    # loop para pegar todas as palavras (puxa uma palavra do arquivo por loop)
    for palavra in arquivo:
        # formato minha variável
        palavra = palavra.strip().upper()
        # acrescento os valores do arquivo na lista
        palavras.append(palavra)

    # Fecha o arquivo
    arquivo.close()

    # cria um número aleatório
    numero = random.randrange(0, len(palavras))

    # Atribui randomicamente um valor para a variável
    palavra = palavras[numero]

    # acrescenta "_" para cada letra que a palavra possui

    lista_letras = ["_" for letra in palavra]

    # começa como False pois ele ainda não foi enforcado (perdeu o jogo)
    enforcou = False
    erros = 0

    # começa como False pois ele ainda não acertou a palavra INTERIA (ganhou o jogo)
    acertou = False

    # Mostra quantas letras a palavra tem
    print(lista_letras)
    print("---------------------")
    # Enquanto "enforcou" e "acertou" não virarem True, o laço continua
    while not enforcou and not acertou:
        chute = input("Digite uma letra: ")
        # formata o chute e trasforma em maiuscula
        chute = chute.strip().upper()

        if chute in palavra:
            # variável 0 para que a letra possa ser localizada novamente sem interferir no valor da posicao
            posicao = 0
            print("---------------------")
            print("Você acertou!")
            # A letra de número (X) da minha (palavra) será colocada na posição (X) da minha lista de (letras_acertadas)
            for letra in palavra:
                if chute.upper() == letra.upper():
                    lista_letras[posicao] = letra
                posicao += 1
        else:
            print("---------------------")
            print("Você errou!")
            erros += 1
            restantes = 6 - erros
            print(f"Você ainda tem {restantes} tentativas")

        if erros == 6:
            print("---------------------")
            print("Você Perdeu!")
            enforcou = erros == 6
            break
        if "_" not in lista_letras:
            print(lista_letras)
            print("---------------------")
            print("Você Venceu!")
            acertou = "_" not in lista_letras
            break

        print(lista_letras)
        print("---------------------")

    print("Fim do jogo!")
