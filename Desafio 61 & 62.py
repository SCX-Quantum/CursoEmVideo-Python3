# =======================================
#         ARITHMETIC PROGRESSION
#    Displaying the First 10 Terms of a PA
# =======================================

# === Layout and ANSI from base_layout.py ===

RESET       = '\033[m'
BOLD        = '\033[1m'
GREEN       = '\033[1;32m'
RED         = '\033[1;31m'
CYAN        = '\033[1;36m'
YELLOW      = '\033[1;33m'

def line():
    print(30 * (f'{CYAN}|{YELLOW}=') + f'{CYAN}|{RESET}')

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
    print("Thanks for using the PA generator!".center(60))
    line()

def ask_number(msg: str) -> int:
    while True:
        try:
            return int(input(f'{msg} '))
        except ValueError:
            print(f'{RED}Please enter a valid integer number.{RESET}')

def ask_continue() -> bool:
    while True:
        choice = input('Do you want to generate another PA? [S] [N]: ').strip().upper()
        if choice in ['S', 'N']:
            return choice == 'S'
        print(f'{RED}Invalid command. Try again.{RESET}')


# === PA Generator Logic ===

def generate_pa(first_term: int, ratio: int, total_terms: int = 10):
    pa_terms = []
    for i in range(total_terms):
        term = first_term + i * ratio
        pa_terms.append(term)
    return pa_terms

def show_pa(pa_terms: list[int]):
    print(f'The first {len(pa_terms)} terms of the PA are:')
    print(f'{BOLD}', end='')
    for term in pa_terms:
        print(f'{term}', end=' → ')
    print(f'END{RESET}')


# === Main Application ===

def main():
    title("ARITHMETIC PROGRESSION")
    section("Enter the first term and the common difference")

    app_on = True
    while app_on:
        a1 = ask_number("First term:")
        r = ask_number("Common difference (razão):")
        print()
        line()
        print()
        pa = generate_pa(a1, r)
        show_pa(pa)
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
