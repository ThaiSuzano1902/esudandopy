"""
#Uma pessoa vai no fliperama e de acordo com o brinquedo, ele da o valor e sabera as horas de jogo.
"""
boliche = 25
pescaria = 15
toboga = 30

print("     Brinquedos\n" 
        "1- Boliche\n"
        "2- Pescaria\n"
        "3- Toboga")

brinquedo = int(input("Escolha o brinquedo: "))
if brinquedo == 1:
    print("Boliche\n"
          "25$_1h")
    horas = int(input ("Voce deseja jogar por 1h, 2h ou 3h?: "))
    if horas == 1:
        print("O valor total vai ser 25$")
    elif horas == 2:
        print("O valor total é de 50$")
    else:
        print("O valor total é de 75$")
elif brinquedo == 2:
    print(" Pescaria\n"
            "15R$_1h")
    horas = int(input ("Voce deseja jogar por 1h, 2h ou 3h?: "))
    if horas == 1:
        print("O valor total vai ser 15$")
    elif horas == 2:
        print("O valor total é de 30$")
    else:
        print("O valor total é de 45$")
else:
    print("Taboga\n"
          "40R$_1h")
    horas = int(input ("Voce deseja jogar por 1h, 2h ou 3h?: "))
    if horas == 1:
        print("O valor total vai ser 40$")
    elif horas == 2:
        print("O valor total é de 80$")
    else:
        print("O valor total é de 120$")
