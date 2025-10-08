

# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

month_date = {

    "january": 31, "february":29, "march":31, "april":30, "may":31, "june":30,
    "july":31, "august":31, "september":30, "october":31, "november":30, "december":31
}

def check_date(month, day):

    if isinstance(month, int):
        if 1 <= month <= 12:
            if 1 <= int(day) <= list(month_date.values())[month - 1]:
                return True
            
    elif isinstance(month, str):
        if month in month_date and 1 <= int(day) <= month_date[month]:
            return True
        
    return False

def main():
    while True:
        date = input('Date: ').strip().lower()
        if '/' in date:
            try:
                month, day, year = map(int, date.split('/'))
                if  check_date(month, day):
                    print(f'{year}-{month:02d}-{day:02d}')
                    break
            except:
                pass
        else:
            try:
                month, year = date.split(',')
                name, day = month.split(' ')
                if check_date(name, day):
                    print(f'{year}-{(list(month_date.keys()).index(name) + 1):02d}-{int(day):02d}')
                    break
            except:
                pass

if __name__ == "__main__":
    main()

