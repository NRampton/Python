class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *args):
        for element in args:
            if isinstance(element, int):
                self.result += element
            elif isinstance(element, list):
                for val in range(len(element)):
                    self.result += element[val]
            elif isinstance(element, tuple):
                for val in range(len(element)):
                    self.result += element[val]
        return self

    def subtract(self, *args):
        for element in args:
            if isinstance(element, int):
                self.result -= element
            elif isinstance(element, list):
                for val in range(len(element)):
                    self.result -= element[val]
            elif isinstance(element, tuple):
                for val in range(len(element)):
                    self.result -= element[val]
        return self


md = MathDojo()
print md.add(2).add(2, (5, 2)).subtract([3, 2], [4, 5, 6], (2, 3)).result

# Code currently supports only unidimensional lists or tuples.
