import logging
from logging.config import fileConfig

fileConfig('config.ini')

from person import Person

#imoprted the function for counting levels
from level_counter import level_counter 


# create an instance of logger
#sample = logging.Logger(__name__, level=logging.INFO)

# creating the file format
#fileformat = logging.Formatter('%(asctime)s | %(name)-10s | %(levelname)-16s | %(msecs)s | %(message)s')
#streamformat = logging.Formatter('%(asctime)s | %(name)-10s | %(message)s')

# defining a handler for streaming in a file
#fh = logging.FileHandler('sample.log')
#fh.setFormatter(fileformat)

# defining a handler for streaming in console
#sh = logging.StreamHandler()
#sh.setFormatter(streamformat)
#sh.setLevel(logging.ERROR)

# adding hanlders to logger
#sample.addHandler(fh)
#sample.addHandler(sh)

sample = logging.getLogger('sample')


# Main code not changed 
##############################################
def sub(a, b):
    if b != 0:
        sample.debug('a / b = ' + str(a / b), exc_info=1)
        return a / b
    
    else:
        sample.info('Divide by zero!')
        return 'a'

print(sub(2, 3))
print(sub(2, 0))

p1 = Person('ali', 'alavi', 23)
p2 = Person('gholi', 'gholami', -23)
##############################################

try:
    print(level_counter('person.log', logging.WARNING))
    print(level_counter('sample.log', logging.INFO))

except FileNotFoundError:
    sample.error('File not found for checking levels', exc_info=True)

except:
    print('Instance of log level not found')

