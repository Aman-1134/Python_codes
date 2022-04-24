class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee("Aman", "Ansari", 50000)
emp_2 = Employee("Vinay", "Sah", 40000)

print(emp_1)
print(emp_1.first)
print(emp_2.email)

print(emp_2.fullname())
