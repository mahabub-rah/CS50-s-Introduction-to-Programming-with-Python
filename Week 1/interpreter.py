ex = input('Expression: ').split(' ')

if '+' in ex:
    num = float(int(ex[0])+int(ex[-1]))
    print(f'{num:.1f}')
elif '-' in ex:
    num = float(int(ex[0])-int(ex[-1]))
    print(f'{num:.1f}')
elif '*' in ex:
    num = float(int(ex[0])*int(ex[-1]))
    print(f'{num:.1f}')
elif '/' in ex:
    num = float(int(ex[0])/int(ex[-1]))
    print(f'{num:.1f}')
