# =========================================================
#         VERIFICAÇÃO DE PARÊNTESES EM EXPRESSÕES
#  Verifica se os parênteses foram abertos e fechados corretamente
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

def ask_expression(msg: str = "Digite uma expressão matemática: ") -> str:
    return input(YELLOW + msg + RESET)

# === Verificação de parênteses ===

def parenteses_balanceados(expressao: str) -> bool:
    pilha = []
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha:
                return False
            pilha.pop()
    return not pilha

# === Lógica principal do desafio ===

def run_challenge():
    expressao = ask_expression()
    if parenteses_balanceados(expressao):
        print(GREEN + "Parênteses corretamente balanceados!" + RESET)
    else:
        print(RED + "Parênteses incorretamente balanceados!" + RESET)

# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("VERIFICAÇÃO DE PARÊNTESES", "Análise de expressão matemática")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
