def main():
    while True:
        try:
            user = input('Fraction: ').strip()
            percent = convert(user)
            print(gauge(percent))
            break
        except ValueError:
            print('Write the correct value.')
        except ZeroDivisionError:
            print("Don't use zero at denominator.")


def convert(fraction):
    if not isinstance(fraction, str) or fraction.count('/') != 1:
        raise ValueError

    numerator, denominator = map(int, fraction.split('/'))

    if denominator == 0:
        raise ZeroDivisionError
    if numerator > denominator or numerator < 0 or denominator < 0:
        raise ValueError

    frac = numerator / denominator
    return round(frac * 100)


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == '__main__':
    main()
