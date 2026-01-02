class Book:
    def __init__(self, title, author, year):
        self.title = title     
        self.author = author    
        self.year = year        
    # def __str__(self):
    #     return f"'{self.title}' — {self.author}, {self.year}"
    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

book1 = Book("Преступление и наказание", "Ф.М. Достоевский", 1866)
print(book1.get_info())
