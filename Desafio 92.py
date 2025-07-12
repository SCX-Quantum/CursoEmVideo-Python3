# =========================================================
#            Cadastro e Aposentadoria de Trabalhador
#    Coleta dados pessoais e calcula idade de aposentadoria
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

def ask_str(prompt: str) -> str:
    return input(prompt).strip()

def ask_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print(f"{RED}Digite um número inteiro válido.{RESET}")

def ask_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print(f"{RED}Digite um número válido (ex: 1500.00).{RESET}")

# === Lógica principal do desafio ===

from datetime import date

def run_challenge():
    atual = date.today().year
    trabalhador = {}

    nome = ask_str("Nome: ")
    nasc = ask_int("Ano de nascimento: ")
    ctps = ask_int("Número da carteira de trabalho (0 se não tiver): ")

    trabalhador['Nome'] = nome
    trabalhador['AnoNascimento'] = nasc
    trabalhador['IdadeAtual'] = atual - nasc
    trabalhador['CTPS'] = ctps

    if ctps != 0:
        ano_contratacao = ask_int("Ano de contratação: ")
        salario = ask_float("Salário (R$): ")
        trabalhador['AnoContratacao'] = ano_contratacao
        trabalhador['Salario'] = salario
        trabalhador['IdadeAposentadoria'] = (ano_contratacao + 35) - nasc

    print("\nInformações do Trabalhador:")
    print("-" * 60)
    for chave, valor in trabalhador.items():
        print(f"{chave:<20}: {valor}")
    print("-" * 60)

# === Função principal ===

def main():
    header("Cadastro Trabalhador", "Cálculo de Aposentadoria")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
