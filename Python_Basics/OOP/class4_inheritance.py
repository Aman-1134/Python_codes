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
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)      #or use Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees == None:
            employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullname())

emp_1 = Developer("Aman","Ansari", 50000, 'Python')
emp_2 = Developer("Vinay", "Sah" , 40000, 'Java')
print(emp_1.prog_lang)

mgr_1 = Manager('Aryan', 'Ansari', 90000, [emp_1])
print(mgr_1.email)
mgr_1.print_emp()
print(mgr_1.employees)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
