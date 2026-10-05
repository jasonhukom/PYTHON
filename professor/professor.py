import random

def main():
    question = {
        "x": [],
        "y": []
    }
    point = 0
    chances = 0
    times = 0
    level = get_level()
    for _ in range(10):
        try:
            int_x = generate_integer(level)
            int_y = generate_integer(level)
        except ValueError:
            break
        else:
            question['x'].append(int_x)
            question['y'].append(int_y)

    while not times >= 10:
        try:
            if not chances >= 3:
                x = question['x'][times]
                y = question['y'][times]
                prompt = f'{x} + {y} = '
                answer = int(input(prompt))
            else:
                break
        except ValueError:
            print('EEE')
            chances  += 3
            continue
        else:
            if answer == x + y:
                point += 1
                times += 1
            else:
                print('EEE')
                chances += 1
                continue
    print(f"Score: {point}")


def get_level():
    while True:
        try:
            n = int(input('Level: '))
        except ValueError:
            pass
        else:
            match n:
                case 1 | 2 | 3:
                    return n
                case _:
                    pass

def generate_integer(level):
    r = lambda x, y: random.randint(x, y)
    if level == 1:
        return r(0, 9)
    elif level == 2:
        return r(10, 99)
    elif level == 3:
        return r(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
