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
                    data.append({
                        'first': parts[1].strip(),
                        'last': parts[0].strip(),
                        "house": line.get('house')
                        })
        field = ['first', 'last', 'house']
        with open(after_filename,'w') as file:
            data = csv.DictWriter(f, fieldnames=field)
            data.writeheader()
            for info in students:
                data.writerow(info)
if __name__ == "__main__":
    main()