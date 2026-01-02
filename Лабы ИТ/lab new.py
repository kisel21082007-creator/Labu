#1.2
with open('example.txt', 'r') as file:
    text = file.read()
print(text)
#1.3
met = int(input('Введите 1 (чтение целиком) или 2 (чтение по строчкам)'))
if met == 1:
    with open('example.txt', 'r') as file:
        text12 = file.read()
    print(text12)
else:
    with open('example.txt', 'r') as file:
        for line in file:
            print(line)
#2.1
izm = str(input('Введите текст -'))
file2 = open('user_input.txt', 'a')
file2.write(izm)
file2.close()
with open('user_input.txt') as file:
    tex = file.read()
print(tex)
#3.1
try:
    with open('net', 'r') in file:
        rer = file.read()
except FileNotFoundError:
    print('Таково файла не существует')