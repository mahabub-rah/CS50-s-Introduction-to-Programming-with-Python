import sys

def find_file_line(filename):
    count = 0
    search_term = filename.replace(".py", "").strip()
    found = False
    with open(filename, "r") as f:
        for data in f:
            remove_space = data.strip()
            if remove_space.startswith('#') and search_term in remove_space:
                found = True
                continue
            if found:
                if remove_space.startswith('#'):
                    break
                if remove_space:
                    count += 1

    return count


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



