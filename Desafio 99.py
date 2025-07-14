# =========================================================
#                  ANÁLISE DO MAIOR VALOR
#       Lê vários números e mostra o maior entre eles
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

def ask_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(RED + "Por favor, digite um número inteiro válido." + RESET)


# === Lógica principal do desafio ===

def maior(*valores):
    print(f"\nAnalisando os valores: {valores}")
    if not valores:
        print(RED + "Nenhum valor foi informado." + RESET)
    else:
        max_valor = max(valores)
        print(GREEN + f"O maior valor informado foi: {max_valor}" + RESET)


def run_challenge():
    numeros = []

    while True:
        n = ask_int("Digite um número (ou 999 para parar): ")
        if n == 999:
            break
        numeros.append(n)

    maior(*numeros)


# === Função principal ===

def main():
    header("FUNÇÃO MAIOR", "Descobre o maior valor entre vários")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")


# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
