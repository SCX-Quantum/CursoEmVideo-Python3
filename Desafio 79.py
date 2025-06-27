# =========================================================
#           DESAFIO: VALORES ÚNICOS E CRESCENTES
#   Recebe valores do usuário e exibe apenas os únicos,
#           ordenados de forma crescente no final.
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

def ask_int(prompt: str = "Digite um número: ") -> int:
    """Solicita um número inteiro do usuário, com validação."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"{RED}Entrada inválida! Digite um número inteiro.{RESET}")

def ask_yes_no(prompt: str = "Deseja continuar? [S/N]: ") -> bool:
    """Retorna True para 'S' e False para 'N', com validação."""
    while True:
        resposta = input(prompt).strip().upper()
        if resposta in ("S", "N"):
            return resposta == "S"
        print(f"{YELLOW}Digite apenas 'S' para sim ou 'N' para não.{RESET}")

# === Lógica principal do desafio ===

def run_challenge():
    valores = []

    while True:
        numero = ask_int("Digite um número: ")
        valores.append(numero)

        if not ask_yes_no("Deseja adicionar outro número? [S/N]: "):
            break

    unicos_ordenados = sorted(set(valores))

    print(f"\n{GREEN}Valores únicos em ordem crescente:{RESET}")
    print(unicos_ordenados)

# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("DESAFIO DOS VALORES ÚNICOS", "Coletando e organizando seus dados")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
