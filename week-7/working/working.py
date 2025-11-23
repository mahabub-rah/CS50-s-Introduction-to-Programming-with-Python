import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r'^(\d{1,2})(?:[:\.]?(\d{2}))?\s+(AM|PM)\s*TO\s*(\d{1,2})(?:[:\.]?(\d{2}))?\s+(AM|PM)$'
    check = re.match(pattern, s.strip().upper())
    if not check:
        raise ValueError('Invalid Format')

    hour1 = check.group(1)
    minute1 = 0 if check.group(2) == None else check.group(2)
    period1 = check.group(3)
    hour2 = check.group(4)
    minute2 = 0 if check.group(5) == None else check.group(5)
    period2 = check.group(6)

    def format(h , m, p):
        if not 1 <= h <= 12:
            raise ValueError('Invalid Hours')
        if not 0<=m<=59:
            raise ValueError('Invalid Minutes')
        if p == 'AM':
            return f'{h % 12:02d}:{m:02d}'
        else:
            return f'{h % 12 +12:02d}:{m:02d}'

    return f"{format(int(hour1), int(minute1), period1)} to {format(int(hour2), int(minute2), period2)}"

if __name__ == "__main__":
    main()
