class Employee:
    employees = {}

    #De constructor van de klasse Employee
    def __init__(self,name, role, departement, salary,isTemporary=False):
        self.name = name
        self.role = role
        self.departement = departement
        self.salary = salary
        self.isTemporary = isTemporary
        self.employees[self.name] = self.departement

    #Deze functie berekent het jaarinkomen van de medewerker en laat het inkomen zijn in duizendtallen (i.e. 55000 = 55K)
    def salary_round(self):
        self.salaris = self.salary * 12
        self.salaris = (self.salaris / 1000)
        return round(self.salaris,2)

    #Deze functie telt hoeveel medewerkers werken op een bepaalde afdeling
    def count_employees(self, departement):
        count = 0
        for people in self.employees.values():
            if people == departement:
                count +=1
        return count


    # Repr zorgt ervoor dat de medewerkers die aangemaakt wordne in de list company, op de juiste manier worden ingevoerd.
    # Een list kan normalister maar 1 object appenden. Door middel van repr, komt er maar 1 string binnen via de return
    def __repr__(self):
        return '%s, %s, €%sk, %s'%(self.name, self.role, self.salary_round(), self.isTemporary)

#Deze klasse vertegenwoordigt alle managers in het bedrijf met de daarbijbehorende bonussen
class Management(Employee):
    managers = {}
    def __init__(self, name, role, departement, salary, bonus, isTemporary=False):
        super().__init__(name, role, departement, salary, isTemporary)
        self.bonus = bonus
        self.managers[self.name] = self.departement

    #Deze functie bepaalt wat de bonus van 10 procent is op hun jaarinkomen
    def manager_bonus(self):
        self.salaris = self.salary_round()
        self.mng_bonus = self.salaris * (self.bonus / 100)
        return self.mng_bonus

    #Deze functie berekent de bonus die de managers krijgen aan de hand van de managers bonus + de bonus per medewerker
    def emp_bonus(self):
        employee_bonus = 0.005
        self.count_manager = 0
        #Dit is de bonus die verkregen is door de 10 procent bij het aanmaken van de instantie
        self.eerst_bonus = self.manager_bonus()
        # Er wordt naar elke department van de managers gekeken
        for man in self.managers.values():
            # Wanneer een manager gelijk is aan een afdeling, wordt de counter met 1 verhoogd.
            # Dit zorgt ervoor dat wanneer er 2 managers zijn van dezelfde afdeling, de counter dus op 2 staat in plaats van 1
            if man == self.departement:
                self.count_manager += 1
        #Als de counter dus groter is dan 1 (2 of meerdere managers per department)
        #Wordt de aantal medewerkers onder de manager gedeelt door de aantal managers van de afdeling
        #Is dit niet het geval, dan worden de aantal medewerkers vermenigvuldigt met de employee_bonus
        if self.count_manager > 1:
            self.emp_times_manager = ((self.count_employees(self.departement)/self.count_manager) * employee_bonus)
            self.tweede_bonus = (self.salaris * self.emp_times_manager)
        else:
            self.tweede_bonus = self.salaris * (self.count_employees(self.departement) * employee_bonus)
        #Hier worden de waarden van salary, bonus 1 en bonus 2 bij elkaar opgeteld
        self.manager_salary = self.salaris + self.eerst_bonus + self.tweede_bonus
        return round(self.manager_salary,2)

    #Repr zorgt ervoor dat de medewerkers die aangemaakt wordne in de list company, op de juiste manier worden ingevoerd.
    #Een list kan normalister maar 1 object appenden. Door middel van repr, komt er maar 1 string binnen via de return
    def __repr__(self):
        return '%s, %s, %s, €%ik, %s, %s mensen onder zich'%(self.name, self.role,self.departement,self.emp_bonus(), self.isTemporary, self.count_employees(self.departement))

company = []
company.append(Employee('Johnson', 'sr. clerc', 'finance', 2300, False))
company.append(Management('Bush jr.', 'manager', 'finance', 5400, 10, True))
company.append(Employee('Jasons', 'clerc', 'finance', 1900, False))
company.append(Management('Bushes', 'manager', 'R&D', 5400, 10, True))
company.append(Employee('Hunter', 'researcher', 'R&D', 2300, False))
company.append(Employee('Vries', 'researcher', 'R&D', 2300, False))
company.append(Employee('Locker', 'researcher', 'R&D', 2300, False))
company.append(Management('Schneier', 'manager', 'R&D', 6400, 10, True))
print(Management.managers, Employee.employees)
print('\n')

for employee in company:
    print(employee)

