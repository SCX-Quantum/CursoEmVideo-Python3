# =========================================================
#             DESAFIO - TABELA DO BRASILEIRÃO 2025
#  Mostra classificação, destaques e pesquisa por equipe
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



# === Lógica principal do desafio ===

def run_challenge():
    tabela = (
        "Flamengo", "Botafogo", "Palmeiras", "Athletico-PR", "Bahia",
        "Cruzeiro", "Grêmio", "Internacional", "Atlético-MG", "São Paulo",
        "Fortaleza", "Bragantino", "Juventude", "Criciúma", "Corinthians",
        "Vasco", "Atlético-GO", "Vitória", "Cuiabá", "Fluminense"
    )

    print("Classificação atual:\n")
    for i, time in enumerate(tabela, start=1):
        if i <= 5:
            cor = GREEN
        elif i > len(tabela) - 4:
            cor = RED
        else:
            cor = ""
        print(f"{cor}{i:>2}º - {time}{RESET}")

    print("\nTimes em ordem alfabética:\n")
    for time in sorted(tabela):
        print(f"- {time}")

    print()
    time_escolhido = input(str("Digite o nome do seu time: ")).title()
    if time_escolhido in tabela:
        pos = tabela.index(time_escolhido) + 1
        print(f"\n{GREEN if pos <= 5 else RED if pos > len(tabela) - 4 else ''}Seu time está na {pos}ª posição.{RESET}")
    else:
        print(f"\n{RED}Time não encontrado na tabela do Brasileirão.{RESET}")

# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("TABELA DO BRASILEIRÃO 2025", "Classificação, busca e destaques. -Atualizado em 25/06/25")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
