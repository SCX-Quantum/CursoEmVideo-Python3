# =========================================================
#           PALPITES DA MEGA-SENA AUTOMATIZADOS
#     Gera jogos com 6 números aleatórios e sem repetição
# =========================================================

import random

# === ANSI ===
RESET  = '\033[m'
GREEN  = '\033[1;32m'
YELLOW = '\033[1;33m'

# === Cabeçalho e rodapé ===
def header(title: str, subtitle: str = ""):
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)
    if subtitle:
        print(subtitle.center(60))
        print("=" * 60)
    print()

def goodbye(message: str = "Boa sorte com seus jogos!"):
    print()
    print("=" * 60)
    print(message.center(60))
    print("=" * 60)

# === Entrada segura ===
def ask_int(msg: str) -> int:
    while True:
        try:
            return int(input(YELLOW + msg + RESET))
        except ValueError:
            print(RESET + "Entrada inválida. Digite um número inteiro.")

# === Lógica principal ===
def gerar_jogos(quantidade: int):
    jogos = []
    for _ in range(quantidade):
        jogo = sorted(random.sample(range(1, 61), 6))
        jogos.append(jogo)
    return jogos

def run_challenge():
    qtd = ask_int("Quantos jogos você quer gerar? ")
    jogos = gerar_jogos(qtd)

    print()
    print(GREEN + f"GERANDO {qtd} JOGO(S) PARA A MEGA-SENA:\n" + RESET)
    for i, jogo in enumerate(jogos, 1):
        print(f"Jogo {i:>2}: {jogo}")

# === Função principal ===
def main():
    header("PALPITES DA MEGA-SENA", "6 números por jogo, sem repetições")
    run_challenge()
    goodbye()

# === Ponto de entrada ===
if __name__ == "__main__":
    main()
