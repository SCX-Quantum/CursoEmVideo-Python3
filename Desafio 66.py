# ================================
#     SUM AND COUNT NUMBERS
#    Type numbers until '999'
# ================================

# === ANSI & Layout ===

RESET  = '\033[m'
BOLD   = '\033[1m'
BLUE   = '\033[1;34m'
WHITE  = '\033[1;37m'
MAG    = '\033[1;35m'
CYAN   = '\033[1;36m'
YELL   = '\033[1;33m'
RED    = '\033[1;31m'

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
    print()
    print("Thanks for using this app!".center(60))
    print()
    line()

# === Utility ===

def ask_int(msg: str) -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(f'{RED}Invalid input. Enter an integer!{RESET}')

# === Main Logic ===

def main():
    header("SUM AND COUNT NUMBERS", "Enter numbers until you type '999'")

    total = count = 0
    while True:
        n = ask_int("Enter a number (999 to stop): ")
        if n == 999:
            break
        total += n
        count += 1

    print()
    line()
    print(f'\n{BOLD}You entered {count} numbers. Total sum: {total}.{RESET}\n')
    goodbye()


# === Run App ===
if __name__ == "__main__":
    main()
