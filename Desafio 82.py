# =========================================================
#                DESAFIO: NÚMEROS ORDENADOS
#       Lê números inteiros e separa pares e ímpares
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

def ask_int(msg: str) -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(RED + "Entrada inválida. Digite um número inteiro." + RESET)

def ask_yes_no(msg: str) -> bool:
    while True:
        resposta = input(msg + " [S/N]: ").strip().lower()
        if resposta in ['s', 'sim']:
            return True
        elif resposta in ['n', 'nao', 'não']:
            return False
        else:
            print(YELLOW + "Responda com S (sim) ou N (não)." + RESET)

# === Lógica principal do desafio ===

def run_challenge():
    numeros = []

    while True:
        n = ask_int("Digite um número inteiro: ")
        numeros.append(n)
        if not ask_yes_no("Deseja digitar outro número?"):
            break

    # Ordenação
    numeros.sort()
    pares = sorted([n for n in numeros if n % 2 == 0])
    impares = sorted([n for n in numeros if n % 2 != 0])

    print("\n" + GREEN + "RESULTADOS:" + RESET)
    print(f"Todos os números: {numeros}")
    print(f"Números pares:    {pares}")
    print(f"Números ímpares: {impares}")

# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("DESAFIO DE NÚMEROS", "Leitura e separação de pares e ímpares")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
