from random import randint
from sys import exit

def main():
    while True:
        try:
            n = int(input('Level: '))
            if not n > 0:
                pass
        except ValueError:
            pass
        else:
            answer = randint(1, n)
            while True:
                try:
                    user = int(input('Guess: '))
                except ValueError:
                    pass
                else:
                    if not user > 0:
                        pass
                    elif user < answer:
                        print('Too Small!')
                        pass
                    elif user > answer:
                        print('Too Large!')
                        pass
                    else:
                        print('Just Right!')
                        exit()
if __name__ == '__main__':
    main()
