from tabulate import tabulate
import csv
import sys

def main():
    command = sys.argv
    if len(command) == 1:
        sys.exit("Too few command-line arguments")
    elif len(command) > 2:
        sys.exit("Too many command-line arguments")
    else:
        filename = command[1]
        if not filename.endswith(".csv"):
            sys.exit("Not a CSV file")

    try:
        li =[]
        with open(filename) as file:
            reader = csv.DictReader(file)
            head = reader.fieldnames
            for row in reader:
                li.append(row.values())
        print(tabulate(li, headers=head, tablefmt='grid'))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()




