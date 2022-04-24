class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)      #if no str repr runs

    def __add__(self, other):       #dunder add
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Aman","Ansari", 50000)
emp_2 = Employee("Vinay", "Sah" , 40000)

print(emp_1)
print(repr(emp_1))            #or print(emp_1.__repr__())
print(str(emp_2))

print(emp_2 + emp_1)    #adds pay of both employees
print(len(emp_2))
