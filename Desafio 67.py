# ========================================
#         MULTIPLICATION TABLES
#     Type numbers to see their tabuada
#  (Negative input ends the application)
# ========================================

# === ANSI & Layout ===

RESET = '\033[m'
BOLD  = '\033[1m'
CYAN  = '\033[1;36m'
YELL  = '\033[1;33m'
GREEN = '\033[1;32m'
RED   = '\033[1;31m'
BLUE  = '\033[1;34m'

def line():
    print(30 * (f'{BLUE}|{YELL}=') + f'{BLUE}|{RESET}')

def header(title_msg: str, subtitle_msg: str = ""):
    line()
    print(f'{CYAN}{title_msg.center(60)}{RESET}')
    line()
    if subtitle_msg:
        print(f'\n{YELL}{subtitle_msg.center(60)}{RESET}\n')

def goodbye():
    line()
    print("Thanks for using the multiplication table app!".center(60))
    line()

def ask_int(msg: str) -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(f'{RED}Please enter a valid integer.{RESET}')


# === Core Logic ===

def show_table(n: int):
    print()
    print(f'{BOLD}{GREEN}Tabuada de {n}:{RESET}')
    for i in range(1, 11):
        print(f'{n} x {i:2} = {n*i}')
    print()


# === Main App ===

def main():
    header("MULTIPLICATION TABLES", "Type a number to see its tabuada")

    while True:
        num = ask_int("Enter a number (negative to stop): ")
        if num < 0:
            print()
            break
        print()
        line()
        print()
        show_table(num)
        print()
        line()
        print()

    goodbye()


# === Entry Point ===
if __name__ == "__main__":
    main()
