# =========================================================
#               MATRIZ 3x3 INTERATIVA
#       Preenche uma matriz 3x3 com valores do usuário
# =========================================================

# === ANSI (uso apenas quando necessário) ===

RESET  = '\033[m'
YELLOW = '\033[1;33m'

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
            return int(input(YELLOW + msg + RESET))
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

# === Lógica principal do desafio ===

def run_challenge():
    matriz = []

    for linha in range(3):
        row = []
        for coluna in range(3):
            valor = ask_int(f"Digite o valor para [{linha},{coluna}]: ")
            row.append(valor)
        matriz.append(row)

    print("\nMatriz 3x3 formatada:\n")
    for row in matriz:
        print(" | ".join(f"{n:^5}" for n in row))

# === Função principal ===

def main():
    header("MATRIZ 3X3", "Preenchimento interativo")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
