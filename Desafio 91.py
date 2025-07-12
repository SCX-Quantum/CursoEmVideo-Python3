# =========================================================
#             JOGO DE DADOS ENTRE 4 JOGADORES
#     Cada jogador lança um dado. Vence quem tirar maior.
# =========================================================

from random import randint
from time import sleep

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

# === Lógica principal do desafio ===

def run_challenge():
    from operator import itemgetter

    jogadores = {
        'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6),
    }

    print("Lançando os dados...\n")
    for jogador, valor in jogadores.items():
        print(f"{jogador} tirou {YELLOW}{valor}{RESET} no dado.")
        sleep(1)

    print("\nClassificação final:")
    ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

    for i, (jogador, valor) in enumerate(ranking):
        if i == 0:
            print(f"{GREEN}🥇 {jogador}: {valor} (Vencedor!){RESET}")
        else:
            print(f"   {jogador}: {valor}")

# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("JOGO DE DADOS", "4 Jogadores. Quem tirará o maior número?")
    run_challenge()
    goodbye("Obrigado por jogar com SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
