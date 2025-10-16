import random

level = 0
while True:
    user = input('Level: ')
    if user.isdigit():
        if int(user) >= 1:
            level = int(user)
            break


attempt = 0
number = random.randint(1, 100)

while attempt < level:
    try:
        guess = int(input('Guess: '))
        if guess >=1:
            if guess > number:
                print('Too large!')
            elif guess < number:
                print('Too small!')
            else:
                print('Just right!')
                break
            attempt +=1
    except:
        pass
