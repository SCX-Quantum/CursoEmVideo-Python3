# =======================================
#           SUM AND COUNT NUMBERS
#       Enter numbers until '999' is typed
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
    print("Thanks for using the sum & count app!".center(60))
    line()

def ask_number(msg: str) -> int:
    while True:
        try:
            return int(input(f'{msg} '))
        except ValueError:
            print(f'{RED}Please enter a valid integer number.{RESET}')


# === Logic for Reading and Summing Numbers ===

def sum_numbers_until_sentinel(sentinel: int = 999):
    count = 0
    total = 0
    while True:
        num = ask_number("Enter a number (999 to stop):")
        if num == sentinel:
            break
        total += num
        count += 1
    return count, total


# === Main Application ===

def main():
    title("SUM AND COUNT NUMBERS")
    section("Enter numbers. Type '999' to finish.")

    count, total = sum_numbers_until_sentinel()

    print()
    line()
    print()
    print(f'{BOLD}You entered {count} numbers in total.{RESET}')
    print(f'{BOLD}The sum of all numbers is {total}.{RESET}')
    print()
    line()
    print()

    thank_you()


# === Entry Point ===
if __name__ == "__main__":
    main()
