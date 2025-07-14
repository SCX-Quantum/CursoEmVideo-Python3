# =========================================================
#               CÁLCULO DA ÁREA DE UM TERRENO
#     Lê largura e comprimento e calcula a área total (m²)
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

def ask_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(RED + "Por favor, digite um número válido." + RESET)

# === Lógica principal do desafio ===

def run_challenge():
    print("Informe as dimensões do terreno:")
    largura = ask_float("  Largura (m): ")
    comprimento = ask_float("  Comprimento (m): ")

    area = largura * comprimento

    print()
    print(GREEN + f"A área do terreno é de {area:.2f} m²." + RESET)

# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("CALCULAR ÁREA DE TERRENO", "Informe largura e comprimento em metros")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
