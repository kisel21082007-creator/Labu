text = int(input('Введите 1 (чтение целиком) или 2 (чтение по строчкам)'))
if text == 1:
    with open('example.txt', 'r') as file:
        text2 = file.read()
    print(text2)
else:
    with open('example.txt', 'r') as file:
        for line in file:
            print(line)