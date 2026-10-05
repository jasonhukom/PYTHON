import time
import datetime
import sys
import pyautogui
from random import randint

console = Console()

def main():
    text_to_type = random_the_materials(database())
    text_coloured = change_color(text_to_type)
    custom_input(consol(text_coloured))

def custom_input(prompt):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    buffer = ""
    while True:
        ch = msvcrt.getwch()
        if ch == '\r':  # Enter
            print()
            return buffer
        elif ch == '\b':  # Backspace
            buffer = buffer[:-1]
            sys.stdout.write('\b \b')
            sys.stdout.flush()
        else:
            buffer += ch
            sys.stdout.write(ch)
            sys.stdout.flush()

def random_the_materials(materials):
    random_number = randint(0, len(materials) - 1)
    return materials[random_number]

def change_color(texts):
    text = Text(texts)
    text.stylize("white")
    return text

def database():
    return [
        "aku jalan jalan ke kota bandung"
    ]

if __name__ == "__main__":
    main()