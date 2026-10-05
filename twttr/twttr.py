def main():
    twtter = input('Input: ')
    print(f"Output: {''.join(remove_vowels(ls(twtter)))}")

def ls(word):
    ls_of_char = []
    return (ls_of_char := [word[char:char + 1] for char in range(len(word))])


def remove_vowels(ls_Word):
    vowels = ['A', 'I', 'U', 'E', 'O', 'a', 'i', 'u', 'e', 'o']
    for _ in range(len(ls_Word)):
        for vowel in vowels:
            if vowel in ls_Word:
                ls_Word.remove(vowel)
    return ls_Word

main()
