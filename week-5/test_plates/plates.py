def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if not s[:2].isalpha():
        return False

    if len(s) < 2 or len(s) > 6:
        return False

    if not s.isalnum():
        return False

    number_started = False
    for char in s:
        if char.isdigit():

            if not number_started:

                if char == "0":
                    return False
                number_started = True
        else:
            if number_started:
                return False
    return True


if __name__ == "__main__":
    main()
