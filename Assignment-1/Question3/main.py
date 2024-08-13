import pickle

class Employee:
    def __init__(self, employee_id, name, age, email, position, department, base_salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.email = email
        self.position = position
        self.department = department
        self.base_salary = base_salary
        self.performance = {}

    def update_info(self, name=None, age=None, email=None, position=None, department=None, base_salary=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if email:
            self.email = email
        if position:
            self.position = position
        if department:
            self.department = department
        if base_salary:
            self.base_salary = base_salary

    def add_performance_metric(self, year, metric):
        self.performance[year] = metric

    def calculate_bonus(self, year):
        if year in self.performance:
            return self.base_salary * self.performance[year] / 100
        return 0

    def calculate_annual_salary(self):
        return self.base_salary * 12

    def __str__(self):
        return f"Employee({self.employee_id}, {self.name}, {self.age}, {self.email}, {self.position}, {self.department}, {self.base_salary})"


class Performance:
    def __init__(self, year, rating):
        self.year = year
        self.rating = rating


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, name, age, email, position, department, base_salary):
        if employee_id not in self.employees:
            self.employees[employee_id] = Employee(employee_id, name, age, email, position, department, base_salary)
        else:
            print(f"Employee with ID {employee_id} already exists.")

    def update_employee(self, employee_id, **kwargs):
        if employee_id in self.employees:
            self.employees[employee_id].update_info(**kwargs)
        else:
            print(f"Employee with ID {employee_id} does not exist.")

    def add_performance_metric(self, employee_id, year, metric):
        if employee_id in self.employees:
            self.employees[employee_id].add_performance_metric(year, metric)
        else:
            print(f"Employee with ID {employee_id} does not exist.")

    def calculate_salary_and_bonus(self, employee_id, year):
        if employee_id in self.employees:
            employee = self.employees[employee_id]
            salary = employee.calculate_annual_salary()
            bonus = employee.calculate_bonus(year)
            return salary, bonus
        else:
            print(f"Employee with ID {employee_id} does not exist.")
            return None, None

    def save_data(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.employees, f)
        print(f"Data saved to {filename}.")

    def load_data(self, filename):
        with open(filename, 'rb') as f:
            self.employees = pickle.load(f)
        print(f"Data loaded from {filename}.")

    def display_employees(self):
        for employee_id, employee in self.employees.items():
            print(employee)

    def __str__(self):
        return f"EmployeeManagementSystem({len(self.employees)} employees)"

def main():
    ems = EmployeeManagementSystem()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Add Performance Metric")
        print("4. Calculate Salary and Bonus")
        print("5. Display Employees")
        print("6. Save Data")
        print("7. Load Data")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            employee_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            age = int(input("Enter employee age: "))
            email = input("Enter employee email: ")
            position = input("Enter employee position: ")
            department = input("Enter employee department: ")
            base_salary = float(input("Enter employee base salary: "))
            ems.add_employee(employee_id, name, age, email, position, department, base_salary)

        elif choice == '2':
            employee_id = input("Enter employee ID: ")
            print("Enter the details to update (leave blank to skip):")
            name = input("Enter employee name: ")
            age = input("Enter employee age: ")
            email = input("Enter employee email: ")
            position = input("Enter employee position: ")
            department = input("Enter employee department: ")
            base_salary = input("Enter employee base salary: ")
            ems.update_employee(employee_id,
                                name=name if name else None,
                                age=int(age) if age else None,
                                email=email if email else None,
                                position=position if position else None,
                                department=department if department else None,
                                base_salary=float(base_salary) if base_salary else None)

        elif choice == '3':
            employee_id = input("Enter employee ID: ")
            year = int(input("Enter year: "))
            metric = float(input("Enter performance metric (percentage): "))
            ems.add_performance_metric(employee_id, year, metric)

        elif choice == '4':
            employee_id = input("Enter employee ID: ")
            year = int(input("Enter year: "))
            salary, bonus = ems.calculate_salary_and_bonus(employee_id, year)
            if salary and bonus is not None:
                print(f"Annual Salary: ${salary}")
                print(f"Bonus for {year}: ${bonus}")

        elif choice == '5':
            ems.display_employees()

        elif choice == '6':
            filename = input("Enter filename to save data: ")
            ems.save_data(filename)

        elif choice == '7':
            filename = input("Enter filename to load data: ")
            ems.load_data(filename)

        elif choice == '8':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
