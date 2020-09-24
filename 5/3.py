class Human:
    def __init__(self, name, email = '', gender = ''):
        self.name = name
        self.email = email
        self.gender = gender

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

class Poet(Human):
    def __init__(self, name, email = '', gender = '', gender1 = ''):
        super().__init__(name, email, gender)
        self.gender1 = gender1

    def __str__(self):
        return f'P<{super().__str__()} {self.gender1}>'

class Author(Human):
    def __init__(self, name, author_id, email = '', gender = '', gender1 = ''):
        super().__init__(name, email, gender)
        self.author_id = author_id
        self.gender1 = gender1

    def __str__(self):
        return f'A<{super().__str__()} {self.author_id}>'

class Researcher(Human):
    def __init__(self, name, field, email = '', gender = '', uni = ''):
        super().__init__(name, email, gender)
        self.field = field 
        self.uni = uni

    def __str__(self):
        return f'R<{super().__str__()} {self.field}>'

class Asar:
    count = 0

    def __init__(self, title, owners = []):
        self.title = title 
        if self.__is_valid(owners):
            self.owners = owners
            Asar.count += 1
        
    def __is_valid(self, owners):
        if type(owners) != list:
            owners = list(owners)

        if type(self) == Poem:
            if len(owners) == 1 and type(owners[0]) == Poet:
                return True
            else:
                print('Poet has to be one person!')
                return False

        elif type(self) == Book:
            for author in owners:
                if type(author) != Author:
                    return False
            return True

        elif type(self) == Article:
            for researcher in owners:
                if type(researcher) != Researcher:
                    return False
            return True

        else:
            raise TypeError
    
    def len_owners(self):
        return len(self.owners)

    def __del__(self):
        print(f'deleting {str(self)}')
        Asar.count -= 1

    def __str__(self):
        return self.title + ' ' + str(self.owners)

class Poem(Asar):
    def __init__(self, title, owners = [], lformat = ''):
        super().__init__(title, owners)
        self.lformat = lformat

class Article(Asar):
    def __init__(self, title, owners = [], mag_name = '', pub_year = 0):
        super().__init__(title, owners)
        self.mag_name = mag_name
        self.pub_year = pub_year

class Book(Asar):
    def __init__(self, title, owners = [], isbn = ''):
        super().__init__(title, owners)
        self.isbn = isbn


po = Poem('rod', ["Poet('Rodrik')"])
bo = Book('this', [Author('roni', 123), Author('Marita', 432)])
