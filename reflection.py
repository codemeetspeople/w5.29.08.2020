class Integer:
    def __init__(self, value):
        self.value = int(value)

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value + other.value)
        return NotImplemented


class Float:
    def __init__(self, value):
        self.value = float(value)

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        if isinstance(other, Float):
            return Float(self.value + other.value)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value + other.value)
        return NotImplemented


integer = Integer(5)
float = Float(5)

print(integer + float)
