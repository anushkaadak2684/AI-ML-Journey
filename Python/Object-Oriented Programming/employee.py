from abc import ABC, abstractmethod

class Employee (ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def calculate_salary(self):
        print("Intern salary: 30,000")

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Full time employee salary: 1,00,000")

class ContractEmployee(Employee):
    def calculate_salary(self):
        print("Contract employee salary: 50,000")

intern = Intern()
ft = FullTimeEmployee()
con = ContractEmployee()

intern.calculate_salary()
ft.calculate_salary()
con.calculate_salary()