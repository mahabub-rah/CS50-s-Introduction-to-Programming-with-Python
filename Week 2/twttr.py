vowel = 'AEIOUaeiou'

def convert(text):
    return ''.join([c for c in text if c not in vowel])

def main():
    user_text = input('Input: ')
    print(f'Output: {convert(user_text)}')

if __name__ == "__main__":
    main()
