import emoji

def main():
    user = input('Input: ').lower().strip()
    print(emoji.emojize(f'{user}', language= 'alias'))

if __name__ == '__main__':
    main()

