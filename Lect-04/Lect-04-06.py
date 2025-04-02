# Імітація do-while

def main():
    ans = ''
    magic_word = 'КІНЕЦЬ'
    while ans != magic_word:
        ans = input(f"Для зупинки введіть {magic_word}: ").strip()
    print('Гаразд. До побачення.')

main()
