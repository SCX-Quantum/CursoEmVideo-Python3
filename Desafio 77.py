# =========================================================
#               DESAFIO: IDENTIFICADOR DE VOGAIS
#     Mostra as vogais presentes em 50 palavras da tupla.
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

# (nenhum necessário para este desafio)

# === Lógica principal do desafio ===

def run_challenge():
    palavras = (
        "camelo", "parafuso", "montanha", "rio", "tempo", "sol", "vento", "neve", "chuva", "fogo",
        "areia", "pedra", "tronco", "folha", "raiz", "terra", "cacto", "luz", "pasto", "nuvem",
        "estrela", "planeta", "cometa", "norte", "sul", "leste", "oeste", "bicho", "corvo", "falcao",
        "leao", "tigre", "urso", "cobra", "lagarto", "sapo", "peixe", "polvo", "concha", "ponte",
        "rua", "cidade", "campo", "praia", "ilha", "rocha", "vale", "pico", "gruta", "mundo"
    )

    vogais = {'a', 'e', 'i', 'o', 'u'}

    for palavra in palavras:
        encontradas = []
        for letra in palavra:
            if letra in vogais:
                encontradas.append(letra)
        lista_formatada = ' '.join(encontradas).upper()
        print(f"{palavra.upper():.<20} Suas vogais são: {GREEN}{lista_formatada}{RESET}")


# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("DESAFIO DAS VOGAIS", "Identifique as vogais de cada palavra")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")


# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
