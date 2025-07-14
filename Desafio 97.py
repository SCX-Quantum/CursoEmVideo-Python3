# =========================================================
#            GERADOR DE CABEÇALHOS DECORATIVOS
#    Exibe diferentes estilos de cabeçalho com cores ANSI
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

def ask_str(message: str) -> str:
    return input(message).strip()


# === Lógica principal do desafio ===

def fancy_header(title: str, style: int = 1):
    """Exibe o título com um dos 5 estilos de cabeçalho decorativo."""

    width = 60
    title_centered = title.center(width)

    if style == 1:
        print(GREEN + "+" * width)
        print(title_centered)
        print("+" * width + RESET)

    elif style == 2:
        print(YELLOW + "=" * width)
        print(title_centered)
        print("=" * width + RESET)

    elif style == 3:
        print(RED + "-" * width)
        print(f"{'<' * 5} {title} {'>' * 5}".center(width))
        print("-" * width + RESET)

    elif style == 4:
        print(GREEN + "~" * width)
        print(f"~~ {title.upper()} ~~".center(width))
        print("~" * width + RESET)

    elif style == 5:
        print(YELLOW + "*" * width)
        print(f"* {title} *".center(width))
        print("*" * width + RESET)

    else:
        print("Estilo inválido. Use um número de 1 a 5.")


# === Função principal ===

def run_challenge():
    print("Demonstração dos 5 estilos de cabeçalho:\n")
    for i in range(1, 6):
        fancy_header(f"Exemplo de Cabeçalho {i}", style=i)
        print()


# === Ponto de entrada do programa ===

def main():
    header("GERADOR DE CABEÇALHOS", "Exemplo com múltiplos estilos")
    run_challenge()
    goodbye("Todos os cabeçalhos foram exibidos!")


if __name__ == "__main__":
    main()
