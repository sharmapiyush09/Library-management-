 class book:
        self.author=author
    def __init__(self,title,author,isd):
        self.isd=isd
        self.title=title
    def info(self):
        print(self.title,self.author,self.isd
 b1=book("physics","HC verma","123245")
 b2=book("maths","S dey","2454764")
 #b1.title
 class library:
     def __init__(self,name):
         self.name=name
         self.books=[]
     def add_book(self,book):
          self.books.append(book)
          print(f'Auther {book.author} is added to your library')
     def remove_book(self,isd1):
         for book in books:
             if (book.isd==isd1):
                self.books.remove(book)
             #    print(f"book with isd {isd1} removed from library")
                print("book with isd {isd1} removed from library".formet)
                #return
         print(f"no book is found with isd {isd1}")
     def display(self):
         print(f'books in {self.name} is')
         if not self.books:
             print("no books found")
         for book in self.books:
             book.info()
 l1=library("digital_library")
 l1.add_book(b1)
 l1.add_book(b2)