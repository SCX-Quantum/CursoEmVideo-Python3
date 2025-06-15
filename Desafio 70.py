# ================================================
#              PRODUCT PRICE SURVEY
#   Record and analyze products and their prices
# ================================================

# === ANSI & Layout ===

RESET = '\033[m'
BOLD  = '\033[1m'
YELL  = '\033[1;33m'
GREEN = '\033[1;32m'
RED   = '\033[1;31m'
CYAN  = '\033[1;36m'
PURPLE= '\033[1;35m'

def line():
    print(30 * (f'{PURPLE}|{YELL}=') + f'{PURPLE}|{RESET}')

def header(title_msg: str, subtitle_msg: str = ""):
    line()
    print(f'{CYAN}{title_msg.center(60)}{RESET}')
    line()
    if subtitle_msg:
        print(f'\n{YELL}{subtitle_msg.center(60)}{RESET}\n')

def goodbye():
    line()
    print("Thanks for using the price survey app!".center(60))
    line()

def ask_float(msg: str) -> float:
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print(f'{RED}Please enter a valid price.{RESET}')

def ask_choice(msg: str, options: list[str]) -> str:
    while True:
        choice = input(msg).strip().upper()
        if choice in options:
            return choice
        print(f'{RED}Invalid option. Try again.{RESET}')

# === Product Recording Logic ===

def survey_products():
    total_spent = 0.0
    over_1000_count = 0
    cheapest_price = float('inf')
    cheapest_product = ''

    while True:
        print()
        name = input("Product name: ").strip()
        price = ask_float("Product price (R$): ")

        total_spent += price
        if price > 1000:
            over_1000_count += 1
        if price < cheapest_price:
            cheapest_price = price
            cheapest_product = name

        print()
        line()
        print()
        cont = ask_choice("Do you want to register another product? [Y/N]: ", ['Y', 'N'])
        print()
        line()
        if cont == 'N':
            break

    return total_spent, over_1000_count, cheapest_product, cheapest_price

# === Main Application ===

def main():
    header("PRODUCT PRICE SURVEY", "Register products and analyze their prices")

    total_spent, over_1000, cheapest_name, cheapest_price = survey_products()

    print()
    print(f'{BOLD}Total spent: R${total_spent:.2f}{RESET}')
    print(f'{BOLD}Number of products over R$1000: {over_1000}{RESET}')
    print(f'{BOLD}Cheapest product: {cheapest_name.title()} (R${cheapest_price:.2f}){RESET}')
    print()
    goodbye()


# === Entry Point ===
if __name__ == "__main__":
    main()
