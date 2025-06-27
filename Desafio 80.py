# =========================================================
#         DESAFIO: INSERÇÃO ORDENADA DE 5 NÚMEROS
#   O usuário digita 5 valores e eles são armazenados já
#      em ordem crescente, sem usar o método sort().
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

def ask_int(prompt: str = "Digite um número inteiro: ") -> int:
    """Solicita um número inteiro do usuário, com validação."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"{RED}Entrada inválida! Digite um número inteiro.{RESET}")

# === Lógica principal do desafio ===

def run_challenge():
    numeros = []

    for i in range(5):
        valor = ask_int(f"Digite o {i+1}º número: ")

        if not numeros:
            numeros.append(valor)
        else:
            inserido = False
            for pos, atual in enumerate(numeros):
                if valor < atual:
                    numeros.insert(pos, valor)
                    inserido = True
                    break
            if not inserido:
                numeros.append(valor)

    print(f"\n{GREEN}Números em ordem crescente:{RESET}")
    print(numeros)

# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("DESAFIO DA INSERÇÃO ORDENADA", "Sem usar sort()")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
