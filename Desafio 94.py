# =========================================================
#         Cadastro e Estatísticas de Pessoas
#     Lê nome, sexo e idade de pessoas e analisa dados
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
    while True:
        valor = input(prompt).strip().title()
        if valor:
            return valor
        print(RED + "Entrada inválida. Tente novamente." + RESET)

def ask_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(RED + "Por favor, digite um número inteiro válido." + RESET)

def ask_sex(prompt: str) -> str:
    while True:
        sexo = input(prompt).strip().upper()
        if sexo in ('M', 'F'):
            return sexo
        print(RED + "Sexo inválido. Use apenas 'M' ou 'F'." + RESET)

# === Lógica principal do desafio ===

def run_challenge():
    pessoas = []

    while True:
        print("-" * 40)
        pessoa = {
            "nome": ask_str("Nome: "),
            "sexo": ask_sex("Sexo [M/F]: "),
            "idade": ask_int("Idade: ")
        }
        pessoas.append(pessoa)

        continuar = input("Deseja continuar? [S/N]: ").strip().upper()
        if continuar != 'S':
            break

    total = len(pessoas)
    media_idade = sum(p['idade'] for p in pessoas) / total
    mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'F']
    acima_da_media = [p for p in pessoas if p['idade'] > media_idade]

    print("\n" + "=" * 60)
    print(f"A) Total de pessoas cadastradas: {GREEN}{total}{RESET}")
    print(f"B) Média de idade do grupo: {YELLOW}{media_idade:.1f} anos{RESET}")
    print(f"C) Lista de mulheres: {', '.join(mulheres) if mulheres else 'Nenhuma mulher cadastrada.'}")
    print("D) Pessoas com idade acima da média:")

    if acima_da_media:
        for p in acima_da_media:
            print(f"   - {p['nome']} ({p['idade']} anos)")
    else:
        print("   Nenhuma pessoa acima da média.")

# === Função principal ===

def main():
    header("Cadastro de Pessoas", "Análise de Idade e Sexo")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
