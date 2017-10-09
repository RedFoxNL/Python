#OOP in Python van de video's van YouTube

class Employee:
    raise_amt = 1.04

    #De 'constructor' van de klasse Employee
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        self.pay = pay

    #Deze functie geeft de volledige naam weer van de werknemer
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    #Met deze functie kun je een medewerker een bonus geven (emp_1.apply_raise())
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    #De 'constructor' van de klasse Developer
    def __init__(self,first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    #Deze functie print de programmeer taal die de developer beheerst
    def print_prog(self):
        return self.prog_lang

class Manager(Employee):
    #De 'constructor' van de klasse Manager
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
           self.employees = []
        else:
            self.employees = employees

    #Deze functie voegt een medewerker toe aan de manager
    def add_emp(self, emp):
        if emp is not self.employees:
            self.employees.append(emp)

    #Deze functie verwijdert een medewerker van de manager
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    #Deze functie print alle medewerkers uit die werken onder de manager
    def print_emp(self):
        for emp in self.employees:
            print("--->",emp.fullname())

emp_1 = Employee('Vera','Moda',40000)
dev_1 = Developer('Thom','Boer',50000, 'Python')
mng_1 = Manager('Ted','Baker',100000, [emp_1] )

print(emp_1.fullname())
print(dev_1.fullname())
print(mng_1.fullname())
print('\n')

print(emp_1.email)
print(dev_1.email)
print(mng_1.email)
print('\n')

mng_1.print_emp()
mng_1.add_emp(dev_1)
mng_1.print_emp()
mng_1.remove_emp(emp_1)
mng_1.print_emp()