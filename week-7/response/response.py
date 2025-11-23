import validators

def main():
    print(check(input('write your mail: ')))

def check(e):
 b = validators.email(e)
 if b:
    return "valid"
 else:
    return 'Invalid'



if __name__ == '__main__':
    main()