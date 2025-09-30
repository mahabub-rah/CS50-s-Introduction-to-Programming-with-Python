def main():
    user_text = input('camelCase: ')
    print(f'snake_case: {convert(user_text)}')

def convert(camel):
    snake = ""
    for c in camel:
        if c.isupper():
            snake += "_" + c.lower()
        else:
            snake += c
    return snake


if __name__ == "__main__":
    main()



