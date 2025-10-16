import random

def main():
    level = get_level()
    score = 0  

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        tries = 0

        while tries < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")  
            tries += 1

        if tries == 3:
            print(f"{x} + {y} = {correct_answer}")


    print(score)

def get_level():
    while True:
        user = input('Level: ')
        if user.isdigit() and int(user) in range(1, 4):
            return int(user)

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
