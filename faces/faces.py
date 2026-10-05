def convert():
    assign = str(input())
    if assign.lower().title() == 'Hello :) Goodbye :(':
        print(assign.replace(':)', '🙂').replace(':(', '🙁'))
    elif assign[-2:] == ':)':
        print(f'{assign[0:-2]}🙂')
    elif assign [-2:] == ':(':
        print(f'{assign[0:-2]}🙁')

convert()
