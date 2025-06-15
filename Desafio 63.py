# =======================================
#         FIBONACCI SEQUENCE
#        Displaying N Fibonacci Terms
# =======================================

# === Layout and ANSI from base_layout.py ===

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
    print("Thanks for using the Fibonacci generator!".center(60))
    line()

def ask_number(msg: str) -> int:
    while True:
        try:
            n = int(input(f'{msg} '))
            if n <= 0:
                print(f'{RED}Please enter a number greater than 0.{RESET}')
            else:
                return n
        except ValueError:
            print(f'{RED}Please enter a valid integer number.{RESET}')

def ask_continue() -> bool:
    while True:
        choice = input('Do you want to generate another sequence? [S] [N]: ').strip().upper()
        if choice in ['S', 'N']:
            return choice == 'S'
        print(f'{RED}Invalid command. Try again.{RESET}')


# === Fibonacci Logic ===

def generate_fibonacci(n_terms: int) -> list[int]:
    sequence = []
    a, b = 0, 1
    for _ in range(n_terms):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def show_fibonacci(sequence: list[int]):
    print(f'The first {len(sequence)} terms of the Fibonacci sequence:')
    print(f'{BOLD}', end='')
    for number in sequence:
        print(f'{number}', end=' → ')
    print(f'END{RESET}')


# === Main Application ===

def main():
    title("FIBONACCI SEQUENCE")
    section("Enter how many terms you want to generate")

    app_on = True
    while app_on:
        n = ask_number("How many terms?")
        print()
        line()
        print()
        fib_sequence = generate_fibonacci(n)
        show_fibonacci(fib_sequence)
        print()
        line()
        print()
        app_on = ask_continue()
        print()
        line()
        print()

    thank_you()


# === Entry Point ===
if __name__ == "__main__":
    main()
