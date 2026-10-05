def main():
    greeting = input('Greeting: ')
    good_Greet = greeting.strip().lower()
    greetingsEveryone(good_Greet)

def greetingsEveryone(good_Greet):
    if good_Greet[0:5:] == 'hello':
        print('$0')
    elif good_Greet[0:1:] == 'h':
        print('$20')
    else:
        print('$100')

main()
