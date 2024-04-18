class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        
    def getPrice(self):
            if hasattr(self, "discount"):
                return self.price - (self.price - self.discount)
            else:
                return self.price
            
    def setDiscount(self, amount):
            self.discount = amount
            
    def __str__(self):
         price = str(self.price)
         return f"Our book for sale:  {self.title} is now on discount {price}"
     
# create an instance
book1 = Book("Harry Potter", "J. k. Rowling", 234, 25.99)
book2 = Book("The Gita", "valmiki", 555, 99.99)
book3 = Book("Comics", "T. V.", 1107, 18.07)

# test 1
print(book1)
print(book2.setDiscount(30))
book2.getPrice()
print(book2)
print(book3.setDiscount(10))
book3.getPrice()
print(book3)

            
