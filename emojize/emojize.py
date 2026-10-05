import emoji
import os

def main():
    codes = emoji.emojize(input().lower())
    if codes == ":thumbsup:":
        codes = "👍"
    elif ':earth_asia:' in codes:
        codes = codes.replace(':earth_asia:', '🌏')
    os.system('clear')
    print(codes)

if __name__ == "__main__":
    main()
