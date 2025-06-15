# ===================================================
#                CASH MACHINE SIMULATOR
#     Withdrawal breakdown using available bills
# ===================================================

# === ANSI & Layout ===

RESET = '\033[m'
BOLD  = '\033[1m'
CYAN  = '\033[1;36m'
YELL  = '\033[1;33m'
GREEN = '\033[1;32m'
RED   = '\033[1;31m'
BLUE  = '\033[1;34m'

def line():
    print(30 * (f'{BLUE}|{GREEN}=') + f'{BLUE}|{RESET}')

def header(title_msg: str, subtitle_msg: str = ""):
    line()
    print(f'{CYAN}{title_msg.center(60)}{RESET}')
    line()
    if subtitle_msg:
        print(f'\n{YELL}{subtitle_msg.center(60)}{RESET}\n')

def goodbye():
    line()
    print("Thanks for using the cash machine simulator!".center(60))
    line()

def ask_int(msg: str) -> int:
    while True:
        try:
            value = int(input(msg))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print(f'{RED}Please enter a valid positive integer amount.{RESET}')

# === Core Logic ===

def breakdown_withdrawal(amount: int):
    bills = [50, 20, 10, 2]
    distribution = {}

    for bill in bills:
        quantity = amount // bill
        if quantity > 0:
            distribution[bill] = quantity
        amount %= bill

    return distribution

def show_distribution(distribution: dict[int, int]):
    print(f'{BOLD}Withdrawal breakdown:{RESET}')
    for bill, qty in distribution.items():
        print(f'{GREEN}{qty}x R${bill} bill(s){RESET}')
    print()

# === Main Application ===

def main():
    header("CASH MACHINE SIMULATOR", "Available bills: R$50, R$20, R$10, R$2")

    amount = ask_int("How much do you want to withdraw (R$): ")

    print()
    line()
    print()
    distribution = breakdown_withdrawal(amount)
    show_distribution(distribution)

    goodbye()


# === Entry Point ===
if __name__ == "__main__":
    main()
