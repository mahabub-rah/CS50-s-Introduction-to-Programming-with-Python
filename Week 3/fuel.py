def main():
    v = False
    while not v:
        try:
            frac = input('Fraction: ').strip()
            numerator, denominator = frac.split('/')
            percentage = (int(numerator) /int(denominator)) * 100
            if percentage >= 2 and percentage <= 98 :
                print(f'{round(percentage)}%')
                v = True
            elif percentage == 100 or percentage == 99:
                print('F')
                v = True
            elif percentage == 0 or percentage == 1:
                print('E')
                v = True
            else:
                print(None)
        except ValueError:
            print(' Write the correct value')
        except ZeroDivisionError:
            print("Don't use zero at numerator")



if __name__ == '__main__':
    main()
