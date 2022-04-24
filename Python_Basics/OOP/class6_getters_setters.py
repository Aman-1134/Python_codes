class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None
        print('Name Deleted')

emp_1 = Employee("Aman","Ansari", 50000)
emp_2 = Employee("Vinay", "Sah" , 4000)

emp_2.fullname = 'Amit Safi'
print(emp_2.fullname)
print(emp_2.email)

del emp_2.fullname        #deletes the full name of emp_2
print(emp_2.fullname)