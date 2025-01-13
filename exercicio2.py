"""
criar lista de alunos

criar um lista de alunos e cada um deles tem sua "ficha"
Dps eles fazer a médai deles e pegar essa média
Para no final comparar entre os aluos qual teve a maior e menor nota.

criar lista de alunos com seu numero de chamada
calcular a media  de cada um, e depois mostrar a lista de todos os 
alunos com sua média, mostrando quem se destacou mais com um print
"""

while True:

    print(" LISTA DE ALUNOS: \n"
        "João , 1 \n"
        "Jhonatan, 2 \n"
        "Thaisa, 3 \n"
        "Maria, 4 \n")

    print("Para sair do programa digite 0\n"
          "Digite 5 para comparar todas médias")
    aluno = int(input("Qual e o seu número de chamada? "))
    print(aluno)

    if aluno == 0:
        break

    if aluno == 1:
        print("Digite de 0 a 100 as notas nas 5 matérias, para mostrarmos se você está ou não aprovado!")
        print("Média das matérias bimestrais\n"
            "História: \n"
            "Geografia: \n"
            "Matématica: \n"
            "Portugues: \n" 
            "Ciencias: \n")

        historia = int(input("Digite a tua nota de 0 a 100 em História: "))
        geografia = int(input("Digite a tua nota de 0 a 100 em Geografia: "))
        matematica = int(input("Digite a sua nota de 0 a 100 em Matématica: "))
        portugues = int(input("Digite a sua nota de 0 a 100 em Portugues "))
        ciencias = int(input("Digite a sua nota de 0 a 100 em Ciencias: "))

        media = (historia + geografia + matematica + portugues + ciencias) / 5
        joao = media
        print(f" A média de Joao e {joao}")

    elif aluno == 2:
        print("Digite de 0 a 100 as notas nas 5 matérias, para mostrarmos se você está ou não aprovado!")
        print("Média das matérias bimestrais\n"
            "História: \n"
            "Geografia: \n"
            "Matématica: \n"
            "Portugues: \n" 
            "Ciencias: \n")
        
        historia = int(input("Digite a tua nota de 0 a 100 em História: "))
        geografia = int(input("Digite a tua nota de 0 a 100 em Geografia: "))
        matematica = int(input("Digite a sua nota de 0 a 100 em Matématica: "))
        portugues = int(input("Digite a sua nota de 0 a 100 em Portugues "))
        ciencias = int(input("Digite a sua nota de 0 a 100 em Ciencias: "))

        media = (historia + geografia + matematica + portugues + ciencias) / 5
        jhonatan = media
        print(f" A média de Jhonatan e {jhonatan}")
        
    elif aluno == 3:
        print("Digite de 0 a 100 as notas nas 5 matérias, para mostrarmos se você está ou não aprovado!")
        print("Média das matérias bimestrais\n"
            "História: \n"
            "Geografia: \n"
            "Matématica: \n"
            "Portugues: \n" 
            "Ciencias: \n")
        
        historia = int(input("Digite a tua nota de 0 a 100 em História: "))
        geografia = int(input("Digite a tua nota de 0 a 100 em Geografia: "))
        matematica = int(input("Digite a sua nota de 0 a 100 em Matématica: "))
        portugues = int(input("Digite a sua nota de 0 a 100 em Portugues "))
        ciencias = int(input("Digite a sua nota de 0 a 100 em Ciencias: "))

        media = (historia + geografia + matematica + portugues + ciencias) / 5
        thaisa = media
        print(f" A média de Thaisa e {thaisa}")
    elif aluno == 4:
        print("Digite de 0 a 100 as notas nas 5 matérias, para mostrarmos se você está ou não aprovado!")
        print("Média das matérias bimestrais\n"
            "História: \n"
            "Geografia: \n"
            "Matématica: \n"
            "Portugues: \n" 
            "Ciencias: \n")
        
        historia = int(input("Digite a tua nota de 0 a 100 em História: "))
        geografia = int(input("Digite a tua nota de 0 a 100 em Geografia: "))
        matematica = int(input("Digite a sua nota de 0 a 100 em Matématica: "))
        portugues = int(input("Digite a sua nota de 0 a 100 em Portugues "))
        ciencias = int(input("Digite a sua nota de 0 a 100 em Ciencias: "))

        media = (historia + geografia + matematica + portugues + ciencias) / 5
        maria = media
        print(f" A média de Mária e {maria}")
    elif aluno == 5:
        lista_notas = [joao, jhonatan, thaisa, maria]
        lista_notas.sort #sort ordena a lista
        print(f"A maior nota e {max(lista_notas)}")
        print(lista_notas)
    else:
        print("Coloque apenas o número da sua chamada, entre 1 a 4")

    
    

