class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


Amit = Employee()
Amit.language = "JavaScript" # This is an instance attribute
print(Amit.language, Amit.salary)
