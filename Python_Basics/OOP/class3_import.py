import datetime
class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #or use Employee.raise_amount() which will be 1.04 even if u update

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def form_string(cls, emp_str):
        first, last, pay = emp_str_1.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            print('Is a Holiday')
        else:
            print('Is a Working Day')


emp_1 = Employee("Aman", "Ansari", 50000)
emp_2 = Employee("Vinay", "Sah", 40000)

Employee.set_raise_amount(1.05)

emp_str_1 = 'Amit-Safi-20000'

new_emp_1 = Employee.form_string(emp_str_1)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(new_emp_1.email)

print(Employee.num_of_emps)

my_day = datetime.date(2019, 10, 21)
Employee.is_workday(my_day)