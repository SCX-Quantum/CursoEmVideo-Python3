# =========================================================
#             DESAFIO - NÚMEROS ALEATÓRIOS
#    Gera 5 números aleatórios e identifica maior e menor
# =========================================================

# === ANSI (uso apenas quando necessário) ===

RESET = '\033[m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
RED = '\033[1;31m'


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

# Nenhuma função necessária para entrada neste desafio.

# === Lógica principal do desafio ===

import random


def run_challenge():
    numeros = tuple(random.randint(1, 1000) for _ in range(5))

    print("Números gerados:\n")
    for i, n in enumerate(numeros, start=1):
        print(f"{i}º número: {n}")

    print()
    print(f"{GREEN}Maior número gerado: {max(numeros)}{RESET}")
    print(f"{RED}Menor número gerado: {min(numeros)}{RESET}")


# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("NÚMEROS ALEATÓRIOS", "Gerador e analisador de 5 inteiros")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")


# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
