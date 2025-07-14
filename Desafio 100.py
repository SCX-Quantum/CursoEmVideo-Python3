# =========================================================
#            SOMA DOS NÚMEROS PARES ALEATÓRIOS
#     Gera 5 números aleatórios e soma apenas os pares
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
# (Não utilizados neste script)

# === Funções principais do desafio ===

from random import randint

def gerar_numeros(qtd=5):
    """Gera uma lista com 'qtd' números aleatórios entre 1 e 100."""
    numeros = [randint(1, 100) for _ in range(qtd)]
    print(f"Números gerados: {YELLOW}{numeros}{RESET}")
    return numeros

def somar_pares(numeros):
    """Soma e exibe apenas os números pares da lista."""
    pares = [n for n in numeros if n % 2 == 0]
    print(f"Números pares: {GREEN}{pares}{RESET}")
    print(f"Soma dos pares: {GREEN}{sum(pares)}{RESET}")

# === Lógica principal do desafio ===

def run_challenge():
    numeros = gerar_numeros()
    somar_pares(numeros)

# === Função principal ===

def main():
    header("SOMA DOS PARES", "Gera 5 números e soma os pares")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
