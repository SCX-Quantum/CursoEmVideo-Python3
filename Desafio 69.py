# ============================================
#         PEOPLE AGE & GENDER SURVEY
#    Collecting and analyzing user data
# ============================================

# === ANSI & Layout ===

RESET = '\033[m'
BOLD  = '\033[1m'
CYAN  = '\033[1;36m'
YELL  = '\033[1;33m'
RED   = '\033[1;31m'
BLUE  = '\033[1;34m'
WHITE = '\033[1;37m'

def line():
    print(30 * (f'{BLUE}|{WHITE}=') + f'{BLUE}|{RESET}')

def header(title_msg: str, subtitle_msg: str = ""):
    line()
    print(f'{CYAN}{title_msg.center(60)}{RESET}')
    line()
    if subtitle_msg:
        print(f'\n{YELL}{subtitle_msg.center(60)}{RESET}\n')

def goodbye():
    line()
    print("Thanks for using the survey tool!".center(60))
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
        print(f'{RED}Invalid option. Try again.{RESET}')

# === Logic for Survey ===

def survey_people():
    over_18 = 0
    men = 0
    women_under_20 = 0

    while True:
        print()
        age = ask_int("Enter age: ")
        gender = ask_choice("Sex: [M] Male | [F] Female: ", ['M', 'F'])

        if age > 18:
            over_18 += 1
        if gender == 'M':
            men += 1
        if gender == 'F' and age < 20:
            women_under_20 += 1

        print()
        line()
        print()
        cont = ask_choice("Do you want to add another person? [Y/N]: ", ['Y', 'N'])
        print()
        line()
        if cont == 'N':
            break

    return over_18, men, women_under_20

# === Main App ===

def main():
    header("PEOPLE AGE & GENDER SURVEY", "Enter details of each person")

    over_18, men, women_under_20 = survey_people()

    print()
    print(f"{BOLD}Number of people over 18: {over_18}{RESET}")
    print(f"{BOLD}Total men registered: {men}{RESET}")
    print(f"{BOLD}Women under 20 years old: {women_under_20}{RESET}")
    print()
    goodbye()


# === Entry Point ===
if __name__ == "__main__":
    main()
