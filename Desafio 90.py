# =========================================================
#              REGISTRO DE ALUNOS E SUAS MÉDIAS
#     Lê nome, média e situação de X alunos e exibe tabela
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
            print(RED + "Por favor, digite um número inteiro válido." + RESET)

def ask_float(msg: str) -> float:
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print(RED + "Por favor, digite um número válido (pode ter casas decimais)." + RESET)

def ask_str(msg: str) -> str:
    value = input(msg).strip()
    return value if value else "(sem nome)"

# === Lógica principal do desafio ===

def run_challenge():
    alunos = []
    quantidade = ask_int("Quantos alunos deseja registrar? ")

    for i in range(1, quantidade + 1):
        print(f"\nAluno {i}:")
        nome = ask_str("  Nome: ")
        media = ask_float("  Média: ")

        if media >= 70.0:
            situacao = "Aprovado"
        elif 50.0 <= media < 70.0:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"

        aluno = {
            "nome": nome,
            "media": media,
            "situacao": situacao
        }

        alunos.append(aluno)

    print("\n" + "=" * 60)
    print("TABELA DE ALUNOS".center(60))
    print("=" * 60)
    print(f"{'NOME':<25}{'MÉDIA':<10}{'SITUAÇÃO':<20}")
    print("-" * 60)

    for aluno in alunos:
        cor = GREEN if aluno['situacao'] == "Aprovado" else YELLOW if aluno['situacao'] == "Recuperação" else RED
        print(f"{aluno['nome']:<25}{aluno['media']:<10.1f}{cor}{aluno['situacao']:<20}{RESET}")

# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("REGISTRO DE ALUNOS", "Médias e Situação Final")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
