# =========================================================
#            CONTADOR E ORDENAÇÃO DE NÚMEROS
#    Lê vários números e exibe estatísticas básicas
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
    """
    Lê um valor inteiro do usuário, repetindo enquanto não for válido.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(f"{RED}Valor inválido! Digite um número inteiro.{RESET}")

# === Lógica principal do desafio ===

def run_challenge():
    numeros = []

    while True:
        n = ask_int(f"Digite um número: ")
        numeros.append(n)

        continuar = input("Deseja continuar? [S/N] ").strip().upper()
        while continuar not in ('S', 'N'):
            print(f"{RED}Opção inválida. Digite S para continuar ou N para parar.{RESET}")
            continuar = input("Deseja continuar? [S/N] ").strip().upper()

        if continuar == 'N':
            break

    print()
    # Quantidade de números lidos
    print(f"Foram digitados {GREEN}{len(numeros)}{RESET} números.")

    # Lista em ordem decrescente
    decrescente = sorted(numeros, reverse=True)
    print(f"Lista em ordem decrescente: {YELLOW}{decrescente}{RESET}")

    # Verifica ocorrência do número 5
    count5 = numeros.count(5)
    if count5 > 0:
        print(f"O número {GREEN}5{RESET} foi digitado {GREEN}{count5}{RESET} vezes.")
    else:
        print(f"O número {RED}5{RESET} não foi digitado nenhuma vez.")

# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("CONTADOR E ORDENAÇÃO", "Estatísticas de números digitados")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
