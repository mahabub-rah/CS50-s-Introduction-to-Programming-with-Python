menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}


item = 0
while True:
    try:
        user_text = input('Item: ').lower().strip()
        if user_text in menu:
            item += menu[user_text]
            print(f'${item:.2f}')
    except EOFError:
        print(f'${item:.2f}')
        break
