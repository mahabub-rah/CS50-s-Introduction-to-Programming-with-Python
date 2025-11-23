import re


def main():
    print(count(input("Text: ")))

def count(s):
    li = re.findall(r'\bum(?=[^\w]|$)', s.lower())
    return len(li)

if __name__ == "__main__":
    main()