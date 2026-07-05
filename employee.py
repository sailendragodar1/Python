class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
employees = []
n = int(input("How many employees? "))
for i in range(n):
    emp_id = int(input("Enter ID: "))
    name = input("Enter name: ")
    salary = float(input("Enter salary: "))
    emp = Employee(emp_id, name, salary)
    employees.append(emp)
print("\nEmployee Details:")
for emp in employees:
    emp.display()
    print()