class NotValidAuthorError(Exception):
    e = 'Author instance not valid!'

    def __str__(self):
        return self.e

    def __repr__(self):
        return self.__str__()

class Author:
    def __init__(self, name, email, gender):
        self.__name = name
        self.__email = email
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def gender(self):
        return self.__gender

class Book:
    currency = 'rial'
    __count = 0

    def __init__(self, name, price, count, authors):
        self.__name = name
        self.__price = price
        Book.__count += count

        if isinstance(authors, list):
            for author in authors:
                if not isinstance(author, Author):
                    raise NotValidAuthorError
            self.__authors = authors
        else:
            if not isinstance(authors, Author):
                raise NotValidAuthorError
            self.__authors = [authors]
        
    def show(self):
        print(f'Title: {self.__name}, Author: {[author.get_name() for author in self.__authors]}, Price: {self.__price}')

    def count():
        return Book.__count


a = [Book('Physics', 12000, 4, Author('Rodrik', 'rodrik.v@gmail.com', 'male')), Book('Physics', 12000, 4, Author('Rodrik', 'rodrik.v@gmail.com', 'male')), Book('Physics', 12000, 4, Author('Rodrik', 'rodrik.v@gmail.com', 'male')), Book('Physics', 12000, 4, Author('Rodrik', 'rodrik.v@gmail.com', 'male'))]
print(Book.count())