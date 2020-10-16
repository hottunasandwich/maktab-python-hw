import logging

# creating an instance of logger
person = logging.getLogger(__name__)

# defining the format of log
#fileformat = logging.Formatter('%(asctime)s | %(name)-10s | %(levelname)-16s | %(msecs)s | %(message)s')

# creating a file handler and setting the format
#fh = logging.FileHandler('person.log')
#fh.setFormatter(fileformat)

# adding the handler to the logger
#person.addHandler(fh)


class Person():
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        person.warning("Person created! {} {}".format(self.name, self.family))
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            person.critical("invalid age!")
            self._age = 0
