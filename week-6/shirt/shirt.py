from PIL import Image, ImageOps
import sys
import os


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        input = sys.argv[1]
        output = sys.argv[2]
        valid = [".jpg", ".jpeg", ".png"]

        if not any(input.lower().endswith(ext) for ext in valid):
            sys.exit('Invalid Input file extension')
        if not any(output.lower().endswith(ext) for ext in valid):
            sys.exit('Invalid Input file extension')
        if os.path.splitext(input)[1].lower() != os.path.splitext(output)[1].lower():
            sys.exit("Input and output have different extensions")
        try:
            input_image = Image.open(input)
        except FileNotFoundError:
            sys.exit("Input does not exist")

        shirt = Image.open('shirt.png')
        size = shirt.size
        fitted_image = ImageOps.fit(input_image, size)
        fitted_image.paste(shirt, mask=shirt)
        fitted_image.save(output)


if __name__ == "__main__":
    main()
