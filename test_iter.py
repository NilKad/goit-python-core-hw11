class Iterrable:
    def __init__(self, some_object, per_page):
        self.some_object = some_object
        self.current = 0
        self.per_page = per_page
        self.acc = []

    def __next__(self):
        # while self.current < len(self.some_object):
        if self.current < len(self.some_object):
            while True:
                self.acc.append(self.some_object[self.current])
                self.current += 1

                if self.current % self.per_page == 0 or self.current >= len(
                    self.some_object
                ):
                    res = self.acc
                    self.acc = []
                    return res

        raise StopIteration


class Library:
    def __init__(self, name):
        self.name = name
        self.lib = []
        self.per_page = 3

    def add_book(self, author, name):
        book = {}
        book["author"] = author
        book["name"] = name
        self.lib.append(book)

    def __iter__(self):
        return Iterrable(self.lib, self.per_page)


my_lib = Library("MyBooks")
print(f"myBooks:{my_lib} ")
my_lib.add_book("Book Autho1", "Book Name1")
my_lib.add_book("Book Autho2", "Book Name2")
my_lib.add_book("Book Autho3", "Book Name3")
my_lib.add_book("Book Autho4", "Book Name4")
my_lib.add_book("Book Autho5", "Book Name5")
my_lib.add_book("Book Autho6", "Book Name6")
my_lib.add_book("Book Autho7", "Book Name7")
my_lib.add_book("Book Autho8", "Book Name8")
my_lib.add_book("Book Autho9", "Book Name9")
my_lib.add_book("Book Autho10", "Book Name10")
my_lib.add_book("Book Autho11", "Book Name11")

for e in my_lib:
    print(e)
