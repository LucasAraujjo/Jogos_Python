import random

def jogar():
    print("---------------------")
    print("Bem vindo ao jogo de adivinhação")
    print("---------------------")

    print("(1) Fácil (2) Médio (3) Difícil")
    dificuldade = int(input("Qual nível de dificuldade? "))

    if (dificuldade == 1):
        print(f"Você digitou: {dificuldade}")
        tentativas = 20
    elif (dificuldade == 2):
        print(f"Você digitou: {dificuldade}")
        tentativas = 10
    else:
        print(f"Você digitou: {dificuldade}")
        tentativas = 5
    print("---------------------")


    numero_secreto = random.randrange(0,101)
    round(numero_secreto)

    pontos = 1000

    for rodada in range (1, tentativas + 1):

        print(f"Rodada {rodada}/{tentativas}")
        chute_str = input("Digite um número entre 0 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)


        if (0 < chute > 100):
            print ("O número que você digitou está fora do limite!")
            continue

        if (rodada == tentativas):
            print("---------------------")
            print(f"O número secreto era: {numero_secreto}")

        acertou = numero_secreto == chute
        maior = chute > numero_secreto

        if (acertou):
            print("Você acertou!")
            print("---------------------")
            break
            
        elif(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
            pontos -= chute
            print(f"Pontos Atuais: {pontos}")
            print("---------------------")
            rodada += 1

        else:
            print("Você errou! O seu chute foi menor que o número secreto.")
            pontos -= chute      
            print(f"Pontos Atuais: {pontos}")
            print("---------------------")
            rodada += 1
    print(f"Pontos Atuais: {pontos}")
    print("Fim do jogo")
