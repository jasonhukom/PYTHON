def main():
    print(f"{check_fuel('Fraction: ')}")


def check_fuel(prompt):
    while True:
        try:
            first_digit, second_digit = input(prompt).split('/')
            first_digit, second_digit = int(first_digit), int(second_digit)
            result = (first_digit / second_digit) * 100
            if first_digit > second_digit or first_digit < 0 or second_digit <= 0:
                continue
            return 'E' if result <= 1 else 'F' if result >= 99 else f'{int(result) if result - int(result) < 0.5 else int(result) + 1}%'

        except ValueError:
            pass
        except ZeroDivisionError:
            if first_digit == 0:
                return 'E'
            else:
                pass

main()
