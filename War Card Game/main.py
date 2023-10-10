import time
from deck import Deck
from player import Player
from war_card_game import WarCardGame

player = Player("Curtis", Deck(is_empty=True))
computer = Player("Computer", Deck(is_empty=True), is_computer=True)
deck = Deck()
auto = True

game = WarCardGame(player, computer, deck)


game.print_welcome_message()
auto = input("\nChoose game type:\n1. Automated\n2. Manual\n")

while not game.check_game_over():
    while auto:
        game.start_battle()
        #time.sleep(0.3)
        game.print_stats()
    else:
        game.start_battle()
        game.print_stats()

        answer = input("\nAre you ready for the next round?\nPress Enter to continue. Enter X to stop.")

        if answer.lower() == "x":
            break


