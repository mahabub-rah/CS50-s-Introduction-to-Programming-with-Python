import argparse, sys
from pyfiglet import Figlet

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--font', help='choose font')

arg = parser.parse_args()

fig = Figlet()

if arg.font:
    try:
        fig.setFont(font=arg.font)
    except:
        sys.exit('Invalid Usage')


user = input('Write your Text: ').strip()
print(fig.renderText(user))