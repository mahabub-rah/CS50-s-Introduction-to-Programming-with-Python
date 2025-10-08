# In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

def main():
    items = []
    counts = {}
    while True:
        try:
            user_input = input().strip().lower()
            if user_input:
                items.append(user_input)
        except EOFError:
            break

    # Count items
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    # Print sorted list in uppercase with counts
    for i in sorted(counts):
        print(f'{counts[i]} {i.upper()}')

if __name__ == "__main__":
    main()
