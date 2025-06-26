# =========================================================
#         DESAFIO - TABELA DE PREÇOS DA PADARIA
#  Lê produtos, ordena por preço e exibe lista organizada
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

'''Nenhuma entrada do usuário necessária para este desafio.'''

# === Lógica principal do desafio ===

def run_challenge():
    produtos_precos = [
        ("CAFÉ PRETO PEQUENO", 1.99),
        ("PÃO DA CHAPA", 3.00),
        ("MISTO QUENTE", 6.00),
        ("MORTADELA TRADICIONAL", 5.99),
        ("BISCOITO DE POLVILHO", 5.99),
        ("PÃO DE QUEIJO COQUETEL", 5.98),
        ("LANCHE NATURAL COM PRESUNTO", 6.50),
        ("PÃO DE QUEIJO MÉDIO", 6.76),
        ("MORTADELA DEFUMADA", 8.99),
        ("COOKIES DE GOTAS DE CHOCOLATE", 9.52),
        ("PÃO DE QUEIJO RECHEADO COM CATUPIRY", 9.89),
        ("PÃO FRANCÊS", 12.00),
        ("BOLO DE FUBÁ", 16.98),
        ("BOLO DE FUBÁ COM GOIABADA", 16.98),
        ("BOLO DE FUBÁ CREMOSO", 16.95),
        ("BOLO DE CHOCOLATE SEM RECHEIO", 15.98),
        ("BOLO DE CENOURA", 15.56),
        ("BOLO DE LARANJA COM CALDA", 17.99),
        ("BOLO FLORESTA NEGRA", 32.55),
        ("BOLO DE CHOCOLATE COM MOUSSE", 32.55),
        ("BOLO DE MORANGO", 36.99),
        ("BAGUETE", 15.00),
        ("BAGUETE COM GERGELIM", 17.98),
        ("MUSSARELA", 17.99),
        ("PÃO ARTESANAL", 22.69),
        ("PÃO SÍRIO", 22.95),
        ("PÃO AUSTRALIANO", 30.66),
        ("PÃO DE FORMA CASEIRO", 30.66),
    ]

    # Organiza por preço
    produtos_ordenados = sorted(produtos_precos, key=lambda x: x[1])

    # Cria a tupla alternando produto e preço
    tabela_tupla = tuple(item for produto in produtos_ordenados for item in (produto[0], produto[1]))

    # Exibe a tabela formatada
    print("Lista de produtos da padaria (do mais barato ao mais caro):\n")
    for nome, preco in produtos_ordenados:
        print(f"{YELLOW}{nome.ljust(45, '.')} R$ {preco:.2f}{RESET}")


# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("TABELA DA PADARIA", "Produtos organizados por preço")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
