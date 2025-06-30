# =========================================================
#             SEPARADOR DE PARES E ÍMPARES
#       Recebe 7 números, separa e ordena
# =========================================================

RESET  = '\033[m'
YELLOW = '\033[1;33m'
GREEN  = '\033[1;32m'

def header(title: str, subtitle: str = ""):
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)
    if subtitle:
        print(subtitle.center(60))
        print("=" * 60)
    print()

def goodbye(message: str = "Fim do programa."):
    print()
    print("=" * 60)
    print(message.center(60))
    print("=" * 60)

def ask_int(msg: str) -> int:
    while True:
        try:
            return int(input(YELLOW + msg + RESET))
        except ValueError:
            print(RESET + "Entrada inválida. Digite um número inteiro.")

def run_challenge():
    numeros = [[], []]  # [pares, impares]

    for i in range(7):
        valor = ask_int(f"Digite o {i+1}º número: ")
        if valor % 2 == 0:
            numeros[0].append(valor)  # pares
        else:
            numeros[1].append(valor)  # ímpares

    numeros[0].sort()
    numeros[1].sort()

    print()
    print(GREEN + f"Pares  : {numeros[0]}")
    print(f"Ímpares: {numeros[1]}" + RESET)

def main():
    header("SEPARADOR DE PARES E ÍMPARES", "Salvando e ordenando valores")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

if __name__ == "__main__":
    main()
