def main():
    time_str = input('What time is it? ')

    float_time = format_checker(time_str.lower().rstrip(' ').lstrip(' '))

    if float_time >= 7.0 and float_time <= 8.0:
        print('breakfast time')
    elif float_time >= 12.0 and float_time <= 13.0:
        print('lunch time')
    elif float_time >= 18.0 and float_time <= 19.0:
        print('dinner time')

def format_checker(format):
    end_char = format[-1]
    try:
        float(end_char)
        return convert(format)

    except ValueError or TypeError:
        t, f = format.split(' ')
        time_converted = convert(t)
        match f:
            case 'a.m.' | 'am' | 'a.m':
                return (time_converted + 12) if time_converted >= 0 and time_converted < 1 else time_converted
            case 'p.m.' | 'pm' | 'p.m':
                return (time_converted + 12) if time_converted >= 1 and time_converted <= 11 else ((time_converted + int(t)) if time_converted == 12 else time_converted)

def convert(time):
    hour, minute = time.split(':')
    return float(hour) + (float(minute) / 60)

if __name__ == "__main__":
    main()
