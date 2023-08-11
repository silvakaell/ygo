from data_yugi import game, lives

print("Yugioh - Você pode derrotar Kaiba?")

is_game_on = False
begin_game = input("Esse é o jogo do Yugi! Deseja começar? S/N: ")
if begin_game == "N":
    print(f'Jogo encerrado! Você terminou com {lives} pontos')
else:
    print(f"Você começa com 2000 pontos de vida!")
    game()
    again = input("Deseja jogar novamente? S/N: ")
    if again == "S":
        game()
    else:
        print("Até a próxima!")