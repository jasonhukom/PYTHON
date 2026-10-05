def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    item_question(menu, "Item: ")

def item_question(menu, prompt):
    price = 0
    while True:
        try:
            item = input(prompt).title()
            price += menu[item]
            price_str = str(price)
            _, seperated_price = price_str.split('.')
            if len(seperated_price) < 2:
                price = price_str + "0"
            print(f"Total: ${price}")
            price = float(price)
        except KeyError:
            if item == '':
                break
            else:
                pass
        except KeyboardInterrupt:
            break
        except EOFError:
            break

main()
