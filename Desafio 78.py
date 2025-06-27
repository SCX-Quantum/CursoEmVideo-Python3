# =========================================================
#          [DESCOBRINDO POSIÇÕES DO MAIOR E MENOR]
#   [Recebe 5 valores, mostra todos, e destaca os extremos]
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

def ask_int(prompt: str) -> int:
    """Solicita ao usuário um número inteiro com validação."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(RED + "Entrada inválida. Por favor, digite um número inteiro." + RESET)

# === Lógica principal do desafio ===

def run_challenge():
    valores = []
    for i in range(5):
        num = ask_int(f"Digite o {i+1}º valor: ")
        valores.append(num)

    print()
    print(YELLOW + "Valores digitados: " + RESET, valores)

    maior = max(valores)
    menor = min(valores)

    pos_maior = [i for i, v in enumerate(valores) if v == maior]
    pos_menor = [i for i, v in enumerate(valores) if v == menor]

    print()
    print(GREEN + f"Maior valor: {maior}" + RESET)
    print(f"Posições do maior valor: {pos_maior}")

    print()
    print(RED + f"Menor valor: {menor}" + RESET)
    print(f"Posições do menor valor: {pos_menor}")

# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("DESAFIO: MAIOR E MENOR COM POSIÇÕES", "Recebe 5 valores e identifica extremos")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
