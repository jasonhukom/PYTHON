def main():
    due = 50
    while due > 0:
        coin = int(input(
f"""Amount Due: {due}
Insert Coin: """
))
        due = coke_machine(due, coin)
    print(f'Change Owed: {due * -1}')

def coke_machine(owe, coin):
    match coin:
        case 25 | 10 | 5:
            return owe - coin
        case _:
            return owe
main()
