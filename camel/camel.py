def main():
    camel = input('camelCase: ')
    check_uppercase(snake_case(camel))
    print()

def snake_case(camelCase):
    casing = []
    for i in range(len(camelCase)):
        casing.append(camelCase[i:i+1])
    return casing

def check_uppercase(ls):
    for char in ls:
        if char.isupper():
            print('_', end='')
        print(char.lower(), end='')

main()
