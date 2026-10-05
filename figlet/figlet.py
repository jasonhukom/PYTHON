import pyfiglet
import sys

def main():
    fonts = sysargv_check()
    while True:
        try:
            if fonts:
                pyfiglet.figlet_format("Error Test",fonts)
            else:
                break
        except pyfiglet.FontNotFound:
            exits_program()
        else:
            break
    text = texts()
    text = ' '.join(text)

    if fonts:
        text_fonted = pyfiglet.figlet_format(text, fonts)
    else:
        text_fonted = pyfiglet.figlet_format(text)
    print(f'Output:\n{text_fonted}')


def sysargv_check():
    font = sys.argv[1:]
    if '-f' in font or '--font' in font:
        return font[-1]
    elif len(font) >= 1 and not ('-f' in font or '--font' in font):
        exits_program()
    else:
        return ''

def texts():
    try:
        text = input('Input: ')
    except (EOFError, KeyboardInterrupt):
        exits_program()
    else:
        text = text.split()
        return text

def exits_program():
    print('Invalid usage')
    sys.exit(1)

if __name__ == "__main__":
    main()
