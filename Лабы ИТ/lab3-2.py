def user_data(filename, content, mode='a'):
    
    if mode == 'w': 
        with open(filename, 'w') as file:
            file.write(content)
    
    elif mode == 'a': 
        with open(filename, 'a') as file:
            file.write('\n' + content)
    
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")

text1 = input("Введите текст для записи: ")
user_data('user_input.txt', text1, mode='w')  

text2 = input("Введите текст для добавления: ")
user_data('user_input.txt', text2, mode='a')  

user_data('файл.txt', '', mode='r')