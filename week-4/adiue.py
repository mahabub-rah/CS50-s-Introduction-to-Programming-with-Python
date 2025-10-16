items = []
while True:
    try:    
        user =input('Name: ').strip()
        items.append(user)
    except EOFError:
        break

text = "Adieu, adieu, to "
if len(items) == 1:
    text = text + items[-1]
else:
    s_item = items[:-1]
    text = (text + ", ".join(s_item)).strip() + ' and ' + items[-1]

print(text)


