import random
import time

seq1 = (1, 2, 3, 4, 5, 6, 7, 9, 11)
tier_1_fight = ["Rei Caveira", "Hellhound", "Sosia", "Ciclope", "Homem-Cogumelo", "Minotauro", "Gárgula",
                "Gyoatan", "Dragão Sombrio", "Geloma", "Mameda"]

tier_1_heal = ["Elfa Mística", "Aliados"]

lives = 2000

dragon = 3000


def dice_maker():
    dice = random.choice(seq1)
    print(f"Você tirou {dice} no dado!")
    return dice


def repeat():
    esc = input("Deseja continuar? S/N: ")
    global is_game_on
    if esc == "N":
        print("Jogo encerrado")
        is_game_on = False

    elif esc == "Y":
        print(lives)
        repeat()
    else:
        game()


def live_points():
    li = random.randint(4, 14)
    f = li * 50
    return f


def game():
    global lives
    global is_game_on

    for _ in range(4):
        valor = dice_maker()
        time.sleep(3)

        if lives <= 0:
            print("Você perdeu!")
            break

        elif valor == 999:
            is_game_on = False
            print("Kaiba te pegou! Fim.")

        elif valor % 2 == 0:
            amount = live_points()
            lives += amount
            print(
                f"Você encontrou {random.choice(tier_1_heal)}, que com seus poderes de cura te deu {amount} pontos de "
                f"vida! Você tem agora {lives} pontos")
            esc = input("Aperte S para continuar ou N para desistir! ")
            if esc == "N":
                print("Jogo encerrado")
                is_game_on = False
                break

        else:
            amount = live_points()
            lives -= amount
            print(
                f"Você encontrou {random.choice(tier_1_fight)} e após uma batalha feroz, derrotou o monstro, com o "
                f"custo de {amount} pontos de vida! Você tem agora {lives} pontos")
            esc = input("Aperte S para continuar ou N para desistir! ")
            if esc == "N":
                print("Jogo encerrado")
                is_game_on = False
                break

    print(f"Você está com {lives} pontos de vida! Fase 2 - O dragão branco lhe aguarda!")
    time.sleep(3)

    for _ in range(3):
        valor = dice_maker()
        time.sleep(3)

        if lives <= 0:
            print("Você perdeu!")
            is_game_on = False
            break

        elif valor == 999:
            is_game_on = False
            print("Kaiba te pegou! Fim.")

        elif valor % 2 == 0:
            amount = live_points()

            if valor == 2 or 4:
                lives += amount * 5
                print(f"Achou um baú e ganhou {amount * 5} pontos de vida! VocÊ está com {lives}")
                esc = input("Aperte S para continuar ou N para desistir! ")
                if esc == "N":
                    print("Jogo encerrado")
                    is_game_on = False
                    break
            else:
                lives += amount * 7
                print(f"Achou um baú e ganhou {amount * 7} pontos de vida! VocÊ está com {lives}")
                esc = input("Aperte S para continuar ou N para desistir! ")
                if esc == "N":
                    print("Jogo encerrado")
                    is_game_on = False
                    break
        else:
            amount = live_points()
            if valor == 1 or 3 or 5:
                lives -= amount * 2
                print(f"Armadilha do Kaiba! Perdeu {amount * 2} pontos de vida! Está com {lives}")
                esc = input("Aperte S para continuar ou N para desistir! ")
                if esc == "N":
                    print("Jogo encerrado")
                    is_game_on = False
                    break
            else:
                print("Você conseguiu fugir da batalha ileso!")
                esc = input("Aperte S para continuar ou N para desistir! ")
                if esc == "N":
                    print("Jogo encerrado")
                    is_game_on = False
                    break

    print(f"DRAGÃO BRANCO APARECE! ELE TEM {dragon} DE VIDA!")
    time.sleep(2)

    if dragon >= lives:
        print("Você perdeu! Deseja jogar novamente?")
    else:
        print("Você ganhou!")
