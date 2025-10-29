import csv
import sys


def main():
    command = sys.argv
    if len(command) < 3:
        sys.exit("Too few command-line arguments")
    elif len(command) > 3:
        sys.exit("Too many command-line arguments")
    else:
        filename = command[1]
        after_filename = command[2]
        if not filename.endswith(".csv"):
            sys.exit("Not a CSV file")

        students = []
        with open(filename) as f:
            reader = csv.DictReader(f)
            for line in reader:
                name = line.get('name')
                if name:
                    parts = name.split(',')
                    students.append({
                        'first': parts[1].strip(),
                        'last': parts[0].strip(),
                        "house": line.get('house')
                        })

        field = ['first', 'last', 'house']

        with open(after_filename,'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=field)
            writer.writeheader()
            for info in students:
                writer.writerow(info)


if __name__ == "__main__":
    main()
