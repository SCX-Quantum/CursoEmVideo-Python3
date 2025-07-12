# =========================================================
#               ANÁLISE DE DESEMPENHO ESPORTIVO
#     Lê dados de um jogador e mostra estatísticas finais
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
    return input(msg).strip()

def ask_int(msg: str) -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(RED + "Por favor, digite um número inteiro válido." + RESET)

# === Lógica principal do desafio ===

def run_challenge():
    jogador = {}
    jogador["nome"] = ask_str("Nome do jogador: ")
    partidas = ask_int(f"Quantas partidas {jogador['nome']} jogou? ")

    gols = []
    for i in range(partidas):
        gol = ask_int(f"  Quantos gols na partida {i + 1}? ")
        gols.append(gol)

    jogador["gols"] = gols
    jogador["total"] = sum(gols)

    print("\n" + GREEN + "===> DADOS DO JOGADOR" + RESET)
    for chave, valor in jogador.items():
        print(f"{chave.capitalize()}: {valor}")

    print("\n" + YELLOW + f"===> DESEMPENHO DE {jogador['nome'].upper()}" + RESET)
    for i, g in enumerate(jogador["gols"]):
        print(f"  → Na partida {i + 1} fez {g} gol(s).")

    print(GREEN + f"\nTotal de gols no campeonato: {jogador['total']}" + RESET)

# === Função principal ===

def main():
    header("ANÁLISE DE JOGADOR", "Estatísticas por partida")
    run_challenge()
    goodbye("Obrigado por usar o analisador SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
