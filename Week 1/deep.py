answer = ['42', 'forty two', 'forty-two']
check = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').lower()
if check.strip() in answer:
    print('Yes')
else:
    print('No')