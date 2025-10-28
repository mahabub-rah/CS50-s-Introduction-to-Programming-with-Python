import sys

def main():
    command = sys.argv
    if len(command) == 1:
        sys.exit("Too few command-line arguments")
    elif len(command) > 2:
        sys.exit("Too many command-line arguments")
    else:
        filename = command[1]
        if not filename.endswith(".py"):
            sys.exit("Not a Python file")

    try:
        with open(filename) as file:
            count = 0
            for line in file:
                line = line.strip()
                if line == "" or line.startswith("#"):
                    continue
                count += 1
        print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")




if __name__ == "__main__":
    main()



