class Indenter():
    def __init__(self):
        self.indent = -1

    def __enter__(self):
        self.indent += 1
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.indent -= 1

    def print(self, s):
        print('\t' * self.indent + s)

a = Indenter()
a.print('as')

with Indenter() as indent:
    indent.print('hi')
    with indent:
        indent.print('How are you!')
        with indent:
            indent.print('Oh my go')

            indent.print('this is pertty cool')

    indent.print('bye')