# Start script

from custom_mod import employee

employee_inst = employee.Employee


emp1 = employee_inst("Zara", 2000)
emp2 = employee_inst("Manni", 5000)

print(employee_inst.empCount)
print(vars(emp1))
print(emp1.name, emp1.salary)


# Same output with diff call:
emp1.displayEmployee()
employee_inst.displayEmployee(emp1)

# Same output with diff call:
employee_inst.displayCount(emp2)
emp1.displayCount()


emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
# del emp1.age  # Delete 'age' attribute.

print(emp1.name, emp1.salary, emp1.age)
print(vars(emp1))

