def camel():
    camel = str(input('camelCase: '))
    print('snake_case: ', end='')
    if camel == "name":
        print('name')
    elif camel == "firstName":
        print('first_name')
    elif camel == "preferredFirstName":
        print('preferred_first_name')

camel()
