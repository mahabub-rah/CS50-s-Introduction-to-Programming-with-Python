# user = '4003600000000014'

def check(user):
    total = 0

    for i, digit in enumerate(map(int, user[::-1])):
        if i % 2 == 1:
            total += digit * 2 - 9 if digit * 2 >= 10 else digit * 2
        else:
            total += digit
    return total


while True:
    user = input("Number: ")

    if not user.isdigit():
        print('foo')
        continue

    elif int(user[:2]) in [34,37] and len(user) == 15:
        if check(user)%10 == 0:
            print('Viva')
            break
    elif int(user[:2]) in [51, 52, 53, 54, 55] and len(user) == 16:
        if check(user)%10 == 0:
            print('MASTERCARD')
            break
    elif int(user[:1]) == 4 and len(user) in [13, 16]:
        if check(user)%10 == 0:
            print('Viva')
            break
    else:
        print("Invalid")
        break

