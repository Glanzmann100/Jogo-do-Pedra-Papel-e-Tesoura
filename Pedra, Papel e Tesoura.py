import random

#Apresenta as Jogadas
Jogadas = ["Pedra", "Papel" , "Tesoura"]
Continuar = True

#Estabeleçe o loop que será executado caso haja empate 
while Continuar:
    Jogador1 = input("Pedra, Papel ou Tesoura? ")
    Jogador2 = random.choice(Jogadas)

#Estabeleçe as condições de vitória, derrota e empate dos jogadores
    if Jogador1 == "Pedra" and Jogador2 == "Tesoura" or Jogador1 == "Papel" and Jogador2 == "Pedra" or Jogador1 == "Tesoura" and Jogador2 == "Papel":
        print(f"Você jogou {Jogador1} e o Adversário jogou {Jogador2} logo você ganhou. ")
        Continuar = False
    elif Jogador1 == Jogador2:
        print("Empate por favor repitam")
    else:
        print(f"O Adversário escolheu {Jogador2} e você {Jogador1} logo você perdeu. ")
        Continuar = False