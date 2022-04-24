import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

#creating db
try:
    c.execute("""create table employees(
                id integer primary key,
                fname text,
                lname text,
                salary integer)

""")
except sqlite3.OperationalError:
    print('Table already exists, so skipping creation')

#insert to db

c.execute("""insert into employees values(1,"Aman","Ansari",1000000)

""")

c.execute("""
insert into employees values (?, ?, ?, ?)

""", (2,"Darsan","Gautam",30000))

c.execute("""
    insert into employees values(:id,:fname, :lname, :salary)
""", {'id' : 3,
     'fname': 'Gopal',
      'lname': 'Khatri',
      'salary': 3000000
})

#query db
c.execute("""
    select * from employees where lname = :last
""",{'last' : 'Gautam'})

print(c.fetchmany(1))

#Update db

c.execute(("""
    select fname,salary from employees where lname = "Ansari"
"""))

print(c.fetchmany(1))
c.execute("""
    update employees set salary = 400000 
        where fname = "Aman" 
""")
c.execute("""
    select * from employees where lname = "Ansari"
""")
print(c.fetchmany(1))

c.execute("""
    update employees set fname ="Lambu"
    where fname = "Darsan"
""")

c.execute("""
    update employees set lname ="Golmal"
    where fname = "Lambu"
""")

c.execute("""
    select * from employees where lname = "Golmal"
""")
print(c.fetchmany(1))

#delete from db

c.execute((""" select * from employees """))
print(c.fetchall())

c.execute("""
    delete from employees where id = 2
""")
c.execute(""" select * from employees""")
print(c.fetchall())

conn.commit()
conn.close()

