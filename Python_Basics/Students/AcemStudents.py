from ACEM import ACEMIANS
class Students(ACEMIANS):
    def __init__(self, name, rollno, faculty, year, part):
        super().__init__(name,rollno, faculty, year, part)
        self.name = name
        self.rollno = rollno
        self.faculty = faculty
        self.year = year
        self.part = part

    def read_info_of_students():
        print("Do the student have middle name?")
        print("Type 'Y' for Yes and 'N' for No")
        x = input()
        if x.upper() == 'Y':
            fname = input("Enter first name of student")
            mname = input("Enter middle name of student")
            lname = input("Enter last name of student")
        else:
            fname = input("Enter first name of student")
            mname = ''
            lname = input("Enter last name of student")
        rollno = input("Enter the roll number")
        faculty = input("Enter faculty")
        year = input("Enter his/her year of studies")
        part = input("Enter part of year:")

    def get_info_of_students(self):
        info_str = f"Student Name:{self.fname} {self.mname} {self.lname } "
        return info_str
    __str__=  get_info_of_students

if __name__ == '__main__':
    stud = Students
    stud.read_info_of_students()
    print(stud.get_info_of_students)


