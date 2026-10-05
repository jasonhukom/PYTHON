def main():
    x, y, z = input('Expression: ').split()
    try:
        x = float(x)
        z = float(z)
    except TypeError:
        print('')
    match y:
        case '+':
            result = x + z
        case '-':
            result = x - z
        case '*':
            result = x * z
        case '/':
            result = x / z
    print(result)

main()
