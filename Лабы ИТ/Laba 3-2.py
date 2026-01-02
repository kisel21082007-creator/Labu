def user_data(filename, content, mode ='a'):
    if mode == 'w':
      with open(filename, 'a') as data:
        data.write(content)
    elif mode == 'a':
      with open(filename, 'r') as file:
       file.write('\n' + content)
try:
    with open('user_input.txt', 'r') as file:
            tex = file.read()
            print(tex)
except FileNotFoundError:
        print('Файл не найден')

userdata = input('Введите текст: ')
user_data('user_input.txt', userdata)