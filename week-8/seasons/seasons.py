from datetime import date
import sys
import inflect

def main():
    birth = input("Date of Birth: ")
    try:
        year, month, day = map(int, birth.split("-"))
        birth_date = date(year, month, day)
    except:
        sys.exit("Invalid Date")

    print(minutes_convert(birth_date))


def minutes_convert(birth_date):
    today = date.today()

    if birth_date > today:
        raise ValueError("Birth date cannot be in the future")
    
    count_days = today - birth_date
    minutes = count_days.days * 24 *60

    p = inflect.engine()
    words = p.number_to_words(minutes, andword='').capitalize()

    return f"{words} minutes"


if __name__ == "__main__":
    main()