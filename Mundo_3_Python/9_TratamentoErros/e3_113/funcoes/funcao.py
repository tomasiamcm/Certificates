
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: O número digitado não é um número válido. Tente novamente!\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[31mERRO: Uusário preferiu não digitar o número.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: O número digitado não é um número real válido!\033[m')
        except (KeyboardInterrupt):
            print('\033[31mERRO: Uusário preferiu não digitar o número.\033[m')
            return 0
        else:
            return n

