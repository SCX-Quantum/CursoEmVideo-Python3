# =======================================
#         FATORIAL CALCULATOR
#    Using the Reusable Layout System
# =======================================

# === ANSI & UI Functions (copied from base_layout.py) ===

RESET       = '\033[m'
BOLD        = '\033[1m'
GREEN       = '\033[1;32m'
RED         = '\033[1;31m'
CYAN        = '\033[1;36m'
YELLOW      = '\033[1;33m'

def line():
    print(30 * (f'{GREEN}|{RED}=') + f'{GREEN}|{RESET}')

def title(text: str):
    line()
    print(f'{CYAN}{text.center(60)}{RESET}')
    line()

def section(text: str):
    print()
    print(f'{YELLOW}{text.center(60)}{RESET}')
    print()

def thank_you():
    line()
    print("Thanks for using the factorial app!".center(60))
    line()

def ask_number(msg: str) -> int:
    while True:
        try:
            return int(input(f'{msg} '))
        except ValueError:
            print(f'{RED}Please enter a valid integer number.{RESET}')

def ask_continue() -> bool:
    while True:
        choice = input('Try another one? [S] [N]: ').strip().upper()
        if choice in ['S', 'N']:
            return choice == 'S'
        print(f'{RED}Invalid command. Try again.{RESET}')


# === Fatorial Calculation ===

def factorial(n: int) -> int:
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

def show_factorial_process(n: int):
    print(f'The factorial of {n} is:')
    print(f'{BOLD}', end='')
    for i in range(n, 0, -1):
        if i != 1:
            print(f'{i} x ', end='')
        else:
            print(f'{i} = ', end='')
    print(f'{factorial(n)}{RESET}')


# === Main Application ===

def main():
    title("FATORIAL CALCULATOR")
    section("Enter an integer number to see its factorial")

    app_on = True
    while app_on:
        number = ask_number("Enter a number:")
        print()
        line()
        print()
        show_factorial_process(number)
        print()
        line()
        print()
        app_on = ask_continue()
        print()
        line()

    thank_you()


# === Entry Point ===
if __name__ == "__main__":
    main()
