#OOP in Python van de video's van YouTube

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.mail = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self,first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def print_prog(self):
        return self.prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
           self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp is not self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("--->",emp.fullname())

emp_1 = Employee('Vera','Moda',40000)
dev_1 = Developer('Thom','Boer',50000, 'Python')
mng_1 = Manager('Ted','Baker',100000, [emp_1] )

print(emp_1.fullname())
print(dev_1.fullname())
print(mng_1.fullname())
mng_1.add_emp(dev_1)
mng_1.print_emp()