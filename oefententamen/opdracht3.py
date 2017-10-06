class Employee:
    def __init__(self,name, role, departement, salary,isTemporary=False):
        self.name = name
        self.role = role
        self.departement = departement
        self.salary = salary
        self.isTemporary = isTemporary

    def __repr__(self):
        self.salary = (self.salary / 1000)
        self.salary = round(self.salary * 12,1)
        if self.role == 'manager':
            self.salary = self.salary *0.10

        return '%s, %s, %s, €%sk, %s'%(self.name, self.role, self.departement, self.salary, self.isTemporary )






class Management(Employee):
    def __init__(self, name, role, departement, salary, bonus, isTemporary=False):
        super().__init__(name, role, departement, salary, isTemporary)
        self.bonus = bonus

    def __repr__(Employee):

"""
(0.5 pt) De klasse Management moet print() van een instantie van deze klasse, vrijwel hetzelfde
weergeven als bij een Employee instantie echter moet bij het jaarlijks inkomen ook de bonus ( is
percentage van het jaar inkomen) verwerkt zijn.
"""





company = []
company.append(Employee('Johnson', 'sr. clerc', 'finance', 2300, False))
company.append(Management('Bush jr.', 'manager', 'finance', 5400, 10, True))
company.append(Employee('Jasons', 'clerc', 'finance', 1900, False))
company.append(Management('Bushes', 'manager', 'R&D', 5400, 10, True))
company.append(Employee('Hunter', 'researcher', 'R&D', 2300, False))
company.append(Employee('Vries', 'researcher', 'R&D', 2300, False))
company.append(Employee('Locker', 'researcher', 'R&D', 2300, False))
company.append(Management('Schneier', 'manager', 'R&D', 6400, 10, True))
# print(Management.managers, Employee.employees)


for employee in company:
    print(employee)

