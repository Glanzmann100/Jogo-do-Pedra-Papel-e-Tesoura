import random

#Pede a jogada de ambos os Jogadores
Jogador1 = input("Pedra, Papel ou Tesoura? ")
Jogador2 = random.choice(["Tesoura", "Papel", "Pedra"])

#Condições onde o Jogador ganha
if Jogador1 == "Pedra" and Jogador2 == "Tesoura":
    print(f" O Adversário jogou {Jogador2} você Ganhou")
elif Jogador1 == "Papel" and Jogador2 == "Pedra":
    print(f" O Adversário jogou {Jogador2} você Ganhou")
elif Jogador1 == "Tesoura" and Jogador2 == "Papel":
    print(f" O Adversário jogou {Jogador2} você Ganhou")
if Jogador1 == Jogador2:
    print("Vocês escolheram o mesmo")

#Caso nenhuma das condições de vitória tenham sido satisfeitas
else:
    print(f"O Adversário jogou {Jogador2} logo ele Ganhou")
