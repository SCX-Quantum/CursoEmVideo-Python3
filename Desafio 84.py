# =========================================================
#            Cadastro de Pessoas com Peso Corporal
#   Lê nome e peso de várias pessoas e analisa os dados.
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
        entrada = input(YELLOW + msg + RESET).strip()
        if not entrada:
            print(RED + "Entrada vazia. Digite um nome válido." + RESET)
        elif entrada.isnumeric():
            print(RED + "Números não são permitidos como nome. Digite um nome válido." + RESET)
        else:
            return entrada

def ask_float(msg: str) -> float:
    while True:
        try:
            return float(input(YELLOW + msg + RESET).replace(",", "."))
        except ValueError:
            print(RED + "Entrada inválida. Digite um número válido." + RESET)

def ask_continue() -> bool:
    while True:
        resp = input(YELLOW + "Deseja continuar? [S/N]: " + RESET).strip().lower()
        if resp in ("s", "n"):
            return resp == "s"
        print(RED + "Resposta inválida. Digite S ou N." + RESET)

# === Lógica principal do desafio ===

def run_challenge():
    pessoas = []

    while True:
        nome = ask_str("Nome: ")
        peso = ask_float("Peso (kg): ")
        pessoas.append({"nome": nome, "peso": peso})

        if not ask_continue():
            break

    print()
    print(GREEN + f"Total de pessoas cadastradas: {len(pessoas)}" + RESET)

    # Descobrindo pesos extremos
    if pessoas:
        pesos = [p["peso"] for p in pessoas]
        max_peso = max(pesos)
        min_peso = min(pesos)

        mais_pesadas = [p["nome"] for p in pessoas if p["peso"] == max_peso]
        mais_leves = [p["nome"] for p in pessoas if p["peso"] == min_peso]

        print()
        print(GREEN + f"{'A' if len(mais_pesadas) == 1 else 'As'} pessoa(s) mais pesada(s): {', '.join(mais_pesadas).title()} ({max_peso} kg)" + RESET)
        print(GREEN + f"{'A' if len(mais_leves) == 1 else 'As'} pessoa(s) mais leve(s): {', '.join(mais_leves).title()} ({min_peso} kg)" + RESET)

# === Função principal ===

def main():
    header("Cadastro de Pesos", "Análise de pessoas cadastradas")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
