# Test-drive a Book class that has attributes for each column 
# in the books table, using the example(s) from your design.

class Book:
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title
        self.author_name = author_name


    def __eq__(self, other):
        return self.__dict__ == other.__dict__


    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author_name})"