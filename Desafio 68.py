# ===========================================
#             PAR OU ÍMPAR GAME
#     Play against the computer. Try to win!
#      Game ends when you lose a round.
# ===========================================

# === ANSI & Layout ===

RESET = '\033[m'
BOLD  = '\033[1m'
CYAN  = '\033[1;36m'
YELL  = '\033[1;33m'
GREEN = '\033[1;32m'
RED   = '\033[1;31m'
MAG   = '\033[1;35m'

from random import randint

def line():
    print(30 * (f'{MAG}|{CYAN}=') + f'{MAG}|{RESET}')

def header(title_msg: str, subtitle_msg: str = ""):
    line()
    print(f'{CYAN}{title_msg.center(60)}{RESET}')
    line()
    if subtitle_msg:
        print(f'\n{YELL}{subtitle_msg.center(60)}{RESET}\n')

def goodbye():
    line()
    print("Thanks for playing! See you next time.".center(60))
    line()

def ask_int(msg: str) -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(f'{RED}Please enter a valid integer.{RESET}')

def ask_choice(msg: str, options: list[str]) -> str:
    while True:
        choice = input(msg).strip().upper()
        if choice in options:
            return choice
        print(f'{RED}Invalid choice. Try again!{RESET}')

# === Game Logic ===

def play_round(player_number: int, choice: str):
    computer_number = randint(0, 500)
    total = player_number + computer_number
    result = "PAR" if total % 2 == 0 else "ÍMPAR"
    print()
    line()
    print(f'\n{BOLD}{GREEN}You played {player_number} and computer played {computer_number}. Total = {total}.{RESET}')
    print(f'{BOLD}Result: {result}{RESET}')
    print()
    line()

    win = (choice == result)
    return win

# === Main App ===

def main():
    header("PAR OU ÍMPAR GAME", "Defeat the computer! (Lose = Game Over)")
    line()

    victories = 0

    while True:
        print()
        choice = ask_choice("Par ou Ímpar? [P/I]: ", ["P", "I"])
        choice = "PAR" if choice == "P" else "ÍMPAR"
        player_number = ask_int("Type your number: ")

        win = play_round(player_number, choice)
        print()

        if win:
            print()
            print(f'{GREEN}You WON this round! Let\'s go again...{RESET}')
            print()
            victories += 1
        else:
            print(f'{RED}You LOST!{RESET}')
            print()
            break

        line()
    line()
    print(f'\n{BOLD}You won {victories} time(s).{RESET}\n')
    goodbye()


# === Entry Point ===
if __name__ == "__main__":
    main()
