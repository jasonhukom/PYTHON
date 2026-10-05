def main():
    n = []
    r = ''
    while True:
        try:
            n.append(input('Name: '))
        except EOFError:
            if len(n) == 1:
                return n[0]
            elif len(n) == 2:
                return f"{n[0]} and {n[1]}"
            else:
                for i in n[:-1]:
                    r += f'{i}, '
                return r + f'and {n[-1]}'

if __name__ == '__main__':
    result = main()
    print(f'\nAdieu, adieu, to {result}')
