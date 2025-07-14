# =========================================================
#                    CONTADOR PERSONALIZADO
#     Conta números com passo, em ordem crescente ou não
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

def ask_int(msg: str) -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(f"{RED}Por favor, digite um número inteiro válido.{RESET}")

# === Lógica principal do desafio ===

def contador(inicio: int, fim: int, passo: int):
    """Realiza uma contagem entre dois números com passo."""
    if passo == 0:
        passo = 1  # Corrigindo passo 0
    if passo < 0:
        passo = -abs(passo)

    print(f"{YELLOW}Contando de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:{RESET}")

    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(f"{i} ", end='', flush=True)
    else:
        for i in range(inicio, fim - 1, -abs(passo)):
            print(f"{i} ", end='', flush=True)
    print("\n")

def run_challenge():
    # Contagem 1 até 10
    contador(1, 10, 1)

    # Contagem 10 até 0
    contador(10, 0, 2)

    # Contagem personalizada
    print(f"{GREEN}Agora é sua vez de personalizar a contagem!{RESET}")
    ini = ask_int("Início: ")
    fim = ask_int("Fim: ")
    passo = ask_int("Passo: ")

    contador(ini, fim, passo)

# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("CONTADOR AUTOMÁTICO", "Mostra contagens variadas")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
