# Python program creating a 
# context manager 

class ContextManager():
    def __init__(self):
        self.indent = -1

    def __enter__(self):
        self.indent += 1
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.indent -= 1

    def print(self, s):
        print('\t' * self.indent + s)

a = ContextManager()
a.print('as')

with ContextManager() as manager:
    manager.print('hi')
    with manager:
        manager.print('How are you!')
        with manager:
            manager.print('Oh my go')

            manager.print('this is pertty cool')

    manager.print('bye')


