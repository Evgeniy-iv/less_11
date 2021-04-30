class ComplexNumber:

    def __init__(self, complex_number):
        self.complex_number = complex_number

    def __add__(self, other):
        return ComplexNumber(self.complex_number + other.complex_number)

    def __mul__(self, other):
        return ComplexNumber(self.complex_number * other.complex_number)

    def __str__(self):
        return f'{self.complex_number}'


if __name__ == '__main__':
    a = complex(2, 5)
    b = complex(3, 7)
    complex_number_1 = ComplexNumber(a)
    complex_number_2 = ComplexNumber(b)
    complex_number_add = complex_number_1 + complex_number_2
    complex_number_mul = complex_number_1 * complex_number_2
    print(complex_number_add)
    print(complex_number_mul)
