# =========================================================
#               MATRIZ 3x3 INTERATIVA
#       Preenche uma matriz 3x3 e faz análises simples
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
    pares = []
    soma_coluna3 = 0

    for linha in range(3):
        row = []
        for coluna in range(3):
            valor = ask_int(f"Digite o valor para [{linha},{coluna}]: ")
            row.append(valor)

            if valor % 2 == 0:
                pares.append(valor)

            if coluna == 2:
                soma_coluna3 += valor

        matriz.append(row)

    print("\nMatriz 3x3 formatada:\n")
    for row in matriz:
        print(" | ".join(f"{n:^5}" for n in row))

    maior_segunda_linha = max(matriz[1])

    print("\nAnálises:\n")
    print(f"- Valores pares digitados: {pares}")
    print(f"- Soma dos valores da 3ª coluna: {soma_coluna3}")
    print(f"- Maior valor da 2ª linha: {maior_segunda_linha}")

# === Função principal ===

def main():
    header("MATRIZ 3X3", "Análises de valores")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
