# refer to Youtube "Python SQLite Tutorial: Complete Overview - Creating a Database, Table, and Running Queries"
# on https://www.youtube.com/watch?v=pd-0G0MigUA by Corey Schafer

import sqlite3 # docu at https://sqlite.org/index.html
from example sqlite employee import Employee

conn = sqlite3.connect(':memory:') # this :memory: is a database file in the memory - Usually with "anything.db" a database file "anything.db"
                                    # would be created every time we run the code, for no errors you need to delete this file again. The "in memory"
                                    # is new with every rund of code
c = conn.cursor()

# could use command "CREATE TABLE IF NOT EXISTS"
c.execute("""CREATE TABLE employees ( 
            first text,
            last text,
            pay integer
            )""")
# Expression Affinity and Declared Type
# TEXT 	"TEXT"
# NUMERIC 	"NUM"
# INTEGER 	"INT"
# REAL 	"REAL"
# BLOB (a.k.a "NONE") 	"" (empty string) 

# insert conn value into database as dictionaries:
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

        # bad praxis would be:
        # c.execute("INSERT INTO employees VALUES ('{}','{}','{}')".format(emp.first, emp.last, emp.pay))
        # better praxis put conn value in as tupels:
        # c.execute("INSERT INTO employees VALUES (?,?,?)", (emp.first, emp.last, emp.pay))


# read values out of database
def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()
# fetchall() gives remaining rows of results, fetchone() next row of result, fetchmany(5) gives max.5 rows of result

# modify values in database
def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

# delete values in database
def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

# using the empolyee class to generate datasets
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

conn.close()

