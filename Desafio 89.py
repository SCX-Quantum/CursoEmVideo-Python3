# =========================================================
#                BOLETIM ESCOLAR SIMPLES
#     Armazena notas, calcula médias e permite consulta
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

def ask_str(msg: str) -> str:
    while True:
        texto = input(YELLOW + msg + RESET).strip()
        if texto and not texto.isdigit():
            return texto
        print(RED + "Entrada inválida. Digite um nome válido." + RESET)

def ask_float(msg: str) -> float:
    while True:
        try:
            return float(input(YELLOW + msg + RESET))
        except ValueError:
            print(RED + "Digite um número válido." + RESET)

# === Lógica principal do desafio ===

def run_challenge():
    alunos = []

    while True:
        nome = ask_str("Nome do aluno (ou 'sair' para encerrar cadastro): ")
        if nome.lower() == 'sair':
            break
        nota1 = ask_float(f"Digite a 1ª nota de {nome}: ")
        nota2 = ask_float(f"Digite a 2ª nota de {nome}: ")
        media = (nota1 + nota2) / 2
        alunos.append([nome, [nota1, nota2], media])
        print(GREEN + f"Aluno {nome} cadastrado com sucesso!\n" + RESET)

    # Exibir boletim geral
    print("\n" + "=" * 60)
    print("BOLETIM GERAL".center(60))
    print("=" * 60)
    print(f"{'Nº':<4} {'Nome':<20} {'Média':>10}")
    print("-" * 60)
    for i, aluno in enumerate(alunos):
        print(f"{i:<4} {aluno[0]:<20} {aluno[2]:>10.2f}")
    print("-" * 60)

    # Consulta individual
    while True:
        nome_busca = ask_str("Digite o nome do aluno para ver notas ou 'sair': ")
        if nome_busca.lower() == 'sair':
            break
        encontrado = False
        for aluno in alunos:
            if aluno[0].lower() == nome_busca.lower():
                print(GREEN + f"\nNotas de {aluno[0]}: {aluno[1][0]} e {aluno[1][1]} | Média: {aluno[2]:.2f}\n" + RESET)
                encontrado = True
                break
        if not encontrado:
            print(RED + "Aluno não encontrado.\n" + RESET)

# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("BOLETIM ESCOLAR", "Cadastro e Consulta de Alunos")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
