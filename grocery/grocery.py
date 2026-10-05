def main():
    list = make_lists()
    dictionary = make_dict(list)
    for times in dictionary:
        print(f'{dictionary[times]} {times}')

def make_lists():
    lists = []
    while True:
        try:
            string = input("")
            string = string.upper()
            if not string:
                raise EOFError
            lists.append(string)
        except EOFError:
            lists = sorted(lists)
            return lists

def make_dict(list):
    dict = {}
    for groceries in list:
        if groceries in dict:
            dict[groceries] += 1
        else:
            dict[groceries] = 1
    return dict

main()
