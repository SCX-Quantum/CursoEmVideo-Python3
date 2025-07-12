# =========================================================
#               ANÁLISE DE DESEMPENHO ESPORTIVO
#     Lê dados de vários jogadores e mostra estatísticas
# =========================================================

# === ANSI (uso apenas quando necessário) ===

RESET = '\033[m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
RED = '\033[1;31m'


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

def cadastrar_jogadores() -> list:
    jogadores = []

    while True:
        jogador = {}
        jogador["nome"] = ask_str("Nome do jogador: ")

        partidas = ask_int(f"Quantas partidas {jogador['nome']} jogou? ")

        gols = []
        for i in range(partidas):
            gol = ask_int(f"  Quantos gols na partida {i + 1}? ")
            gols.append(gol)

        jogador["gols"] = gols
        jogador["total"] = sum(gols)

        jogadores.append(jogador)

        continuar = ask_str("Deseja adicionar outro jogador? [S/N] ").lower()
        if continuar != 's':
            break

    return jogadores


def mostrar_ranking(jogadores: list):
    print("\n" + YELLOW + "RANKING DE JOGADORES POR TOTAL DE GOLS" + RESET)
    print("-" * 60)
    print(f"{'NOME':<20} | {'PARTIDAS':<10} | {'TOTAL DE GOLS':<10}")
    print("-" * 60)

    # Ordena por total de gols decrescente
    for jogador in sorted(jogadores, key=lambda j: j["total"], reverse=True):
        print(f"{jogador['nome']:<20} | {len(jogador['gols']):<10} | {jogador['total']:<10}")
    print("-" * 60)


def mostrar_relatorio(jogadores: list):
    while True:
        nome = ask_str("\nDigite o nome do jogador para ver detalhes (ou 'sair'): ").lower()
        if nome == 'sair':
            break

        jogador_encontrado = next((j for j in jogadores if j["nome"].lower() == nome), None)

        if jogador_encontrado:
            print("\n" + GREEN + f"===> RELATÓRIO DE {jogador_encontrado['nome'].upper()}" + RESET)
            for i, g in enumerate(jogador_encontrado["gols"]):
                print(f"  → Na partida {i + 1} fez {g} gol(s).")
            print(GREEN + f"\nTotal de gols no campeonato: {jogador_encontrado['total']}" + RESET)
        else:
            print(RED + "Jogador não encontrado. Tente novamente." + RESET)


# === Função principal ===

def run_challenge():
    jogadores = cadastrar_jogadores()
    mostrar_ranking(jogadores)
    mostrar_relatorio(jogadores)


# === Função principal do programa ===

def main():
    header("ANÁLISE DE JOGADORES", "Estatísticas por partida")
    run_challenge()
    goodbye("Obrigado por usar o analisador SCX!")


# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
