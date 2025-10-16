text = input('File name: ').lower()
print(text)

if 'png' in text:
    print('image/png')
elif 'jpg' in text:
    print('image/jpeg')
elif 'jpeg' in text:
   print('image/jpeg')
elif 'git' in text:
   print('image/git')
elif 'pdf' in text:
   print('application/pdf')
elif 'zip' in text:
   print('application/zip')
elif 'txt' in text:
    print('application/text')
else:
    print('application/octet-stream')

