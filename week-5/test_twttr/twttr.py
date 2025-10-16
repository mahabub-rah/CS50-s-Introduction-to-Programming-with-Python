def main():
    user_text = input('Input: ')
    print(f'Output: {shorten(user_text)}')

def shorten(word):
    return ''.join([c for c in word if c not in 'AEIOUaeiou'])


if __name__ == "__main__":
    main()
