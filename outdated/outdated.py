MONTH_IN_YEAR = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    day, month, year = get_month()
    print(f"{year}-{month:02}-{day:02}")

def get_month():
    while True:
        day = None
        month = None
        year = None
        formatted_date_month_year = None
        formatted_month_date_year = None
        try:
            date = input("Date: ")
        except (EOFError):
            pass
        else:
            if ('/') in date:
                month, day, year = date.split('/')
                formatted_month_date_year = f"{month}/{day}/{year}"
            else:
                try:
                    for months in MONTH_IN_YEAR:
                        if months in date:
                            month = month_to_integer(months)
                            day, year= date.replace(months, "").strip().replace(" ", "").split(',')
                            formatted_date_month_year = f"{months} {day}, {year}"
                            break
                        else:
                            pass
                except (TypeError, ValueError):
                    pass
        try:
            day = int(day)
            month = int(month)
            year = int(year)
        except (TypeError, ValueError):
            pass
        else:
            if day > 31 or day < 0:
                pass
            elif month > 12 or month < 0:
                pass
            elif year < 0:
                pass
            else:
                if date == formatted_month_date_year or date == formatted_date_month_year:
                    return day, month, year
                else:
                    pass


def month_to_integer(month):
    match month:
        case "January":
            month_number = 1
        case "February":
            month_number = 2
        case "March":
            month_number = 3
        case "April":
            month_number = 4
        case "May":
            month_number = 5
        case "June":
            month_number = 6
        case "July":
            month_number = 7
        case "August":
            month_number = 8
        case "September":
            month_number = 9
        case "October":
            month_number = 10
        case "November":
            month_number = 11
        case "December":
            month_number = 12
    return month_number

main()
