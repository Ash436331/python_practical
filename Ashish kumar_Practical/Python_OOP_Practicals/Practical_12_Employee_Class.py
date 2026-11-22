# Thought of the day: A good object takes care of itself, and a good person takes care of others.
# Practical 12: Employee class
class Employee:
    employee_count = 0

    def __init__(self, name, department, basic, da, hra):
        if basic < 0 or da < 0 or hra < 0:
            raise ValueError("Basic, DA and HRA cannot be negative.")

        self.name = name
        self.department = department
        self.basic = basic
        self.da = da
        self.hra = hra
        Employee.employee_count += 1

    def salary(self):
        return self.basic + self.da + self.hra

    def __del__(self):
        # Reduce the count when an Employee object is destroyed.
        # Skip objects whose __init__ failed validation (they were never counted).
        if hasattr(self, "hra"):
            Employee.employee_count -= 1

    def __str__(self):
        return (
            f"Employee Name: {self.name}\n"
            f"Department: {self.department}\n"
            f"Basic: {self.basic:.2f}\n"
            f"DA: {self.da:.2f}\n"
            f"HRA: {self.hra:.2f}\n"
            f"Total Salary: {self.salary():.2f}"
        )


# Create and display one employee.
try:
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    basic = float(input("Enter basic salary: "))
    da = float(input("Enter DA: "))
    hra = float(input("Enter HRA: "))

    employee = Employee(name, department, basic, da, hra)
    print("\nEmployee details")
    print(employee)
    print("Number of employee objects:", Employee.employee_count)
except ValueError as error:
    print("Invalid input:", error)
