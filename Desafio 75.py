# =========================================================
#         DESAFIO - ANÁLISE DE NÚMEROS DIGITADOS
#  Lê 4 inteiros e analisa quantidade, posição e paridade
# =========================================================

# === ANSI (uso apenas quando necessário) ===

RESET  = '\033[m'
GREEN  = '\033[1;32m'
YELLOW = '\033[1;33m'
RED    = '\033[1;31m'

# === Cabeçalho e rodapé do programa ===

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

# === Utilitários de entrada ===

def ask_int(message: str) -> int:
    while True:
        try:
            return int(input(YELLOW + message + RESET))
        except ValueError:
            print(RED + "Entrada inválida. Digite um número inteiro." + RESET)

# === Lógica principal do desafio ===

def run_challenge():
    print("Digite 4 números inteiros:\n")
    numeros = tuple(ask_int(f"{i+1}º número: ") for i in range(4))

    print("\nAnalisando...\n")

    if 9 in numeros:
        qtd_9 = numeros.count(9)
        print(f"O número 9 apareceu {GREEN}{qtd_9}{RESET} vez(es).")
    else:
        print(RED + "O número 3 não foi digitado." + RESET)

    if 3 in numeros:
        pos_3 = numeros.index(3) + 1
        print(f"O número 3 apareceu pela primeira vez na {GREEN}{pos_3}ª{RESET} posição.")
    else:
        print(RED + "O número 3 não foi digitado." + RESET)

    pares = [n for n in numeros if n % 2 == 0]
    if pares:
        print(f"Números pares digitados: {GREEN}{', '.join(map(str, pares))}{RESET}")
    else:
        print(RED + "Nenhum número par foi digitado." + RESET)

# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("ANÁLISE DE NÚMEROS", "Contagem, posição e números pares")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
