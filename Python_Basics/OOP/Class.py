class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = self.pay* self.raise_amount
        return self.pay


emp_1 = Employee('Aman', 'Ansari', 50000)

print(emp_1.fullname())
emp_1.apply_raise()
print(emp_1.pay)

