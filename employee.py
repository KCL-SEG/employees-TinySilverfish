# Base Employee class
class Employee:
    def __init__(self, name):
        self.name = name
    
    def get_pay(self):
        """Calculate the pay for the employee."""
        raise NotImplementedError
    
    def __str__(self):
        """Return a string representation of the pay calculation."""
        raise NotImplementedError

# Salary Employee subclass
class SalaryEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary
    
    def get_pay(self):
        return self.monthly_salary
    
    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}.  Their total pay is {self.monthly_salary}."

# Hourly Employee subclass
class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def get_pay(self):
        return self.hourly_rate * self.hours_worked
    
    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour.  Their total pay is {self.get_pay()}."

# Bonus Commission decorator class
class BonusCommissionEmployee(Employee):
    def __init__(self, employee, bonus):
        self._employee = employee
        self.bonus = bonus
    
    def get_pay(self):
        return self._employee.get_pay() + self.bonus
    
    def __str__(self):
        base_str = str(self._employee).split(".")[0]  # Extract the base string without the total pay part
        return f"{base_str} and receives a bonus commission of {self.bonus}.  Their total pay is {self.get_pay()}."

# Contract Commission decorator class
class ContractCommissionEmployee(Employee):
    def __init__(self, employee, contracts_landed, commission_per_contract):
        self._employee = employee
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract
    
    def get_pay(self):
        return self._employee.get_pay() + self.contracts_landed * self.commission_per_contract
    
    def __str__(self):
        base_str = str(self._employee).split(".")[0]  # Extract the base string without the total pay part
        return f"{base_str} and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract.  Their total pay is {self.get_pay()}."

# Constructing the employee objects
billie = SalaryEmployee('Billie', 4000)
charlie = HourlyEmployee('Charlie', 25, 100)
renee = ContractCommissionEmployee(SalaryEmployee('Renee', 3000), 4, 200)
jan = ContractCommissionEmployee(HourlyEmployee('Jan', 25, 150), 3, 220)
robbie = BonusCommissionEmployee(SalaryEmployee('Robbie', 2000), 1500)
ariel = BonusCommissionEmployee(HourlyEmployee('Ariel', 30, 120), 600)

# Testing the employees
employee_data = {
    'billie': (billie.get_pay(), str(billie)),
    'charlie': (charlie.get_pay(), str(charlie)),
    'renee': (renee.get_pay(), str(renee)),
    'jan': (jan.get_pay(), str(jan)),
    'robbie': (robbie.get_pay(), str(robbie)),
    'ariel': (ariel.get_pay(), str(ariel))
}

employee_data
