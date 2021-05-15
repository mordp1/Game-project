print("====================")
print("Welcome to the Game")
print("====================")

numero_secreto = 14

chute = input("Digite o numero: ")

print("Seu numero é ", chute)
numero = int(chute)
if(numero_secreto == numero):
    print("Voce acertou")
else:
    print("Você errou")

print ("The End")