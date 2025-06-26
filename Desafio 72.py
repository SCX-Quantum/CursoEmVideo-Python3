# =========================================================
    #                [NÚMEROS POR EXTENSO]
#       [Recebe um imput de numero inteiro e retorna
#       o valor salvo em uma tupla.]
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
    """Solicita um número inteiro e valida a entrada."""
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(f'{RED}Por favor, digite um número inteiro válido.{RESET}')

# === Lógica principal do desafio ===

def run_challenge():
    """
    Recebe um número entre 0 e 100 e exibe sua forma por extenso.
    """
    numeros_extenso = (
        'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',
        'vinte e um', 'vinte e dois', 'vinte e três', 'vinte e quatro', 'vinte e cinco', 'vinte e seis', 'vinte e sete',
        'vinte e oito', 'vinte e nove', 'trinta', 'trinta e um', 'trinta e dois', 'trinta e três', 'trinta e quatro',
        'trinta e cinco', 'trinta e seis', 'trinta e sete', 'trinta e oito', 'trinta e nove', 'quarenta',
        'quarenta e um', 'quarenta e dois', 'quarenta e três', 'quarenta e quatro', 'quarenta e cinco',
        'quarenta e seis', 'quarenta e sete', 'quarenta e oito', 'quarenta e nove', 'cinquenta',
        'cinquenta e um', 'cinquenta e dois', 'cinquenta e três', 'cinquenta e quatro', 'cinquenta e cinco',
        'cinquenta e seis', 'cinquenta e sete', 'cinquenta e oito', 'cinquenta e nove', 'sessenta',
        'sessenta e um', 'sessenta e dois', 'sessenta e três', 'sessenta e quatro', 'sessenta e cinco',
        'sessenta e seis', 'sessenta e sete', 'sessenta e oito', 'sessenta e nove', 'setenta',
        'setenta e um', 'setenta e dois', 'setenta e três', 'setenta e quatro', 'setenta e cinco',
        'setenta e seis', 'setenta e sete', 'setenta e oito', 'setenta e nove', 'oitenta',
        'oitenta e um', 'oitenta e dois', 'oitenta e três', 'oitenta e quatro', 'oitenta e cinco',
        'oitenta e seis', 'oitenta e sete', 'oitenta e oito', 'oitenta e nove', 'noventa',
        'noventa e um', 'noventa e dois', 'noventa e três', 'noventa e quatro', 'noventa e cinco',
        'noventa e seis', 'noventa e sete', 'noventa e oito', 'noventa e nove', 'cem'
    )

    while True:
        numero = ask_int("Digite um número: ")

        if 0 <= numero <= 100:
            print()
            print(f"Você digitou o número {GREEN}{numeros_extenso[numero]}{RESET}.")
            break
        else:
            print(f"{RED}Número fora do intervalo permitido (0 a 100). Tente novamente.{RESET}")


# === Função principal ===

def main():
    """Executa o cabeçalho, o desafio e a finalização do programa."""
    header("NÚMEROS POR EXTENSO", "Digite um número entre 0 e 100 e receba-o escrito na tela.")
    run_challenge()
    goodbye("Obrigado por usar os programas da SCX!")

# === Ponto de entrada do programa ===

if __name__ == "__main__":
    main()
