class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.__is_available = True  
    def is_available(self):
        return self.__is_available
    def check_out(self):
        if self.__is_available:
            self.__is_available = False
            print(f"'{self.title}' has been successfully checked out.")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    def return_item(self):
        self.__is_available = True
        print(f"'{self.title}' has been returned.")

    def get_info(self):
        status = "Available" if self.__is_available else "Checked Out"
        return f"ID: {self.item_id} | Title: {self.title} | Status: {status}"
class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages
    def get_info(self):
        base_info = super().get_info()
        return f"[Book] {base_info} | Author: {self.author} | Pages: {self.pages}"
class DVD(LibraryItem):
    def __init__(self, title, item_id, duration_mins):
        super().__init__(title, item_id)
        self.duration_mins = duration_mins
    def get_info(self):
        base_info = super().get_info()
        return f"[DVD]  {base_info} | Duration: {self.duration_mins} mins"
if __name__ == "__main__":
    book1 = Book("Python Basics", "B101", "Guido van Rossum", 350)
    dvd1 = DVD("Inception", "D202", 148)

    print("--- Initial Item Details ---")
    print(book1.get_info())
    print(dvd1.get_info())

    print("\n--- Borrowing and Returning ---")
    book1.check_out()
    book1.check_out()
    
    book1.return_item()

    print("\n--- Polymorphism Demo (Looping through items) ---")
    items = [book1, dvd1]
    for item in items:
        print(item.get_info())
