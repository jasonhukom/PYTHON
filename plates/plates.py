def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    alphabets = [alphabet for alphabet in "qwertyuiopasdfghjklzxcvbnm"]
    symbols = [symbol for symbol in "`~!@#$%^&*()_-+=[{]}\\|;:'\",<.>/?"]
    numbers = [number for number in "1234567890"]

    charlist = text_to_list(s)
    intlist = list_has_int(s)

    order_number, order_list = find_order(charlist, numbers)

    var_for_alpha = 0
    for char in charlist:
        if (
            len
            (charlist) <= 2
            or len(charlist) > 7
            or len(order_number) > 0
                and (
                    (order_number[0] == 0)
                    or (type(intlist[0]) == int and int(charlist[0]) == order_number[0])
                    or (type(intlist[0]) == int)
                    or (len(order_number) > 0 and intlist[-len(order_number)] != order_number[0])
                )
            ):
            return False
        elif (len(charlist) - 1) == charlist.index(char):
            return True
        elif char in symbols:
            return False
        elif char in alphabets and var_for_alpha < 1:
            continue
        elif char in numbers:
            var_for_alpha += 1
            try:
                int(order_number[-1])
                if order_list[order_list.index(charlist.index(char))] == charlist.index(char):
                    continue
                else:
                    return False
            except:
                continue

def find_order(list_char, number_list):
    order = []
    list_order = []
    loop = len(list_char) + 1
    list_char.append(' ')
    for i in range(loop):
        for char in list_char[i]:
            if char in number_list:
                order.append(int(char))
                list_order.append(i)
    return order, list_order


def text_to_list(t):
    char = []
    for i in range(len(t)):
        char.append(t[i:i + 1].lower())
    return char

def list_has_int(ls):
    char = []
    for i in range(len(ls)):
        try:
            char.append(int(ls[i:i + 1].lower()))
        except ValueError:
            char.append(ls[i:i + 1].lower())
    return char

main()
