class Book:
    def __init__(self,name,author,price,publishing_year):
        self.Book_name=name
        self.Book_author=author
        self.Book_price=price
        self.Book_year=publishing_year
    def add_book(self):
        print("Book Name: "+str(self.Book_name))
        print("Book Author: "+str(self.Book_author))
        print("Book Price: "+str(self.Book_price))
        print("Book was published in : "+str(self.Book_year))
        print("Book added")
    def years_since_published(self):
        years_ago_published=2021-self.Book_year
        print("This book was published "+str(years_ago_published)+" years ago")

Harry_Potter=Book("Harry Potter and Philosopher's Stone","J. K. Rowling",1928,1997)
Harry_Potter.add_book()
Harry_Potter.years_since_published()

Wimpy_Kid=Book("Dairy of a Wimpy Kid","Jeff Kinney",700,2017)
Wimpy_Kid.add_book()
Wimpy_Kid.years_since_published()
