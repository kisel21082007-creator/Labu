def read_file(text, filename):
    if text == 1:
        with open(filename, 'r') as file:
            return file.read()
    else:
        with open(filename, 'r') as file:
          return ''.join([line for line in file])
            
text = int(input('Введите 1 (чтение целиком) или 2 (чтение по строчкам): '))
result = read_file(text, 'example.txt')
print(result)