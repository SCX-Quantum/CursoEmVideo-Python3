# =======================================
#         MIN, MAX AND AVERAGE
#         Reading Numbers Dynamically
# =======================================

# === Layout and ANSI from base_layout.py ===

RESET   = '\033[m'
BOLD    = '\033[1m'
CYAN    = '\033[1;36m'
YELLOW  = '\033[1;33m'
RED     = '\033[1;31m'
GREEN   = '\033[1;32m'
BLUE    = '\033[1;34m'
MAGENTA = '\033[1;35m'
WHITE   = '\033[1;37m'

# === Custom random color line ===
def line():
    print(30 * (f'{MAGENTA}|{CYAN}=') + f'{MAGENTA}|{RESET}')

def title(text: str):
    line()
    print(f'{BLUE}{text.center(60)}{RESET}')
    line()

def section(text: str):
    print()
    print(f'{YELLOW}{text.center(60)}{RESET}')
    print()

def thank_you():
    line()
    print("Thanks for using the analyzer app!".center(60))
    line()

def ask_number(msg: str) -> int:
    while True:
        try:
            return int(input(f'{msg} '))
        except ValueError:
            print(f'{RED}Please enter a valid integer number.{RESET}')

def ask_continue() -> bool:
    while True:
        choice = input('Do you want to enter another number? [S] [N]: ').strip().upper()
        if choice in ['S', 'N']:
            return choice == 'S'
        print(f'{RED}Invalid command. Try again.{RESET}')


# === Logic for Min, Max, and Average ===

def analyze_numbers():
    numbers = []
    while True:
        num = ask_number("Enter a number:")
        numbers.append(num)
        print()
        line()
        print()
        if not ask_continue():
            break
        print()
        line()
        print()

    maximum = max(numbers)
    minimum = min(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average, numbers


# === Main Application ===

def main():
    title("MIN, MAX AND AVERAGE")
    section("Type numbers and get the stats")

    min_val, max_val, avg, all_numbers = analyze_numbers()

    print()
    line()
    print()
    print(f'{BOLD}Numbers entered: {all_numbers}{RESET}')
    print(f'{BOLD}Minimum value: {GREEN}{min_val}{RESET}')
    print(f'{BOLD}Maximum value: {RED}{max_val}{RESET}')
    print(f'{BOLD}Average: {CYAN}{avg:.2f}{RESET}')
    print()

    thank_you()


# === Entry Point ===
if __name__ == "__main__":
    main()
