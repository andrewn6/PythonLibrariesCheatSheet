##Classes and Instances

"""

#Making a class in python
class Employee:
	pass

#Making an instance of the employee class
emp1 = Employee()
emp2 = Employee()

#Assigning class properties/attributes to the instance manually(Which is nonsense)

emp1.firstname = "Hoax"
emp1.lastname = "Snowden"
emp1.pay = 50000
emp1.email = "HoaxSnowden@comp.com"

emp2.firstname = "Test"
emp2.lastname = "User"
emp2.pay = 60000
emp2.email = "TestUser@comp.com"

#Then accessing each variables
print(emp1.firstname)
print(emp2.firstname)

"""

# But we can make a way to make it faster to make a instance of the class without doing the long code above, and it is using constructors inside a class


# Making a class named employee
class Employee:

    ##This is a class variable(can be shared amongst all instance)
    raise_amt = 1.04

    # Lets check the count of each employee
    num_of_emps = 0

    # Make the constructor/initialization
    # self refers to the instance itself
    # Everytime we make a new instance of the class, this method always gets executed
    def __init__(self, first, last, pay):
        # Then make the class properties
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@comp.com"

        # Add a new employee to the num_of_emps
        Employee.num_of_emps += 1

    # Making a class method to get the fullname of a emoloyee
    # We need to pass in the variable 'self' because it is the instance of the class.
    def fullname(self):
        return self.first + " " + self.last

    # Make a method where we can add the raise_amt to our employees pay
    # We used 'Employee.raise_amt' because it is a class variable and it is not under the __init__ method.
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)

    # Making a static method
    # Should always use the @staticmethod
    # This method doesnt have ahy connections with the variables/attributes above, this is just a method in a class and not using self as a parameter.
    @staticmethod
    def isWorkDay(dayNum):
        if dayNum == 5 or dayNumm == 6 and dayNum < 7:
            return False
        else:
            return True

    # At the other side, classmethods are methods that uses 'cls' as its first parameter, class methods can change the class variables or any variables of our class
    # Remember that instance variables and class variables are different
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # We can use classmethod to make a new instance of a class
    @classmethod
    def empFromString(cls, emp_str):
        # Splits the string
        first, last, pay = emp_str.split("-")
        # This is the same as Employee(first, last, pay) but using cls instead of Employee
        return cls(first, last, int(pay))


# Make instance of the employee class with the dunder init(__init__)
# Then pass in the (self, first, last, pay) but self is not included as self refers to "emp1"
emp1 = Employee("Hoax", "Snowden", 50000)

# Anotha one
emp2 = Employee("Test", "User", 60000)

# As we can see this is much more easier and simple than the one in the docstring above, this is way shorter, cleaner and faster

# Print the instance's properties/attributes/variables
print(emp1.first)
print(emp1.email)
print()
print(emp2.first)
print(emp2.email)

# We can print the full name of each employee using f strings or .format
# But this is way too long, and we can just make a normal class method (function is called a method when is inside a class)
print("{} {}".format(emp1.first, emp1.last))

# Lets call the function we made
print(emp1.fullname())
print(emp2.fullname())

print("")

# So basically, emp1.fullname() == Employee.fullname(emp1)
print(Employee.fullname(emp1))


##Class Variables
print(emp1.pay)

##Then we can raise the amount by 4% using the method we made above
print(emp1.pay)
emp1.apply_raise()  # Adds 4% to the emp pay
print(emp1.pay)

print()

# So class variables are like variables that is there already, and cannot be entered by a user and accessible to other instances, another good example is counting the number of employees, i added the code above, check it.
# So right now we have two instances of the class, it is emp1 and emp2, so bascially we have 2 employee, lets check it
print(Employee.num_of_emps)  # 2

# Lets make another employee to test it
emp3 = Employee("Elliot", "Alderson", "100000")
print(Employee.num_of_emps)  # 3

print()

##Staticmethods and Classmethods
# staticmethods are methods that doesnt have any connection with the class, for example, i made a static method in our class Employee above, check it
print(Employee.isWorkDay(5))  # 5 is saturday, 0 is sunday

# classmethods are methods of our class that can change using only the class and without affecting the instance variables or the instance itself
print(Employee.raise_amt)

# Calling the class method
# Like regular methods, class methods do not need to enter 2 arguments, as 'Employee' itself is the 'cls' attrubite in our class method
Employee.set_raise_amt(1.06)
print(Employee.raise_amt)

# Or another use of class method is when we want to use a string delimited with - to make instance of a class

str_emp4 = "John-Doe-70000"
str_emp5 = "Jane-Doe-80000"

# Check the classmethod i made above called empFromString
# Make new instance of the class using string
emp4 = Employee.empFromString(str_emp4)
emp5 = Employee.empFromString(str_emp5)

print(emp4.fullname())
print(emp5.fullname())

##Class inheritance
# You can inherit methods and variables from another class by inheriting it.
# You can inherit a class by doing this
# class NewClass(classWeInheritFrom)
class Developer(Employee):

    # We basically override the raise_amt in the employee, but the raise_amt in employee is still 1.04
    raise_amt = 1.10

    # Then call the same init function
    def __init__(self, first, last, pay, prog_lang):
        # This super().__init__() is going to pass the init method from the Employee class automatically so we dont have to type it
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


# Make instance of the new class that we inherit from the Employee
dev1 = Developer("Miller", "Smith", "50000", "Python")
dev2 = Developer("Blake", "Williams", "40000", "Java")

# Prints it instance variables the same as the Employee
print(dev1.email)
print(dev1.prog_lang)

# Lets see the raise_amt of the two class because they are not the same, Developer and Employee class are different, developer class just inherited the methods and attributes of the Employee class
print(Employee.raise_amt)
print(Developer.raise_amt)

# We can also make a manager class from the Employee class

print()


class Manager(Employee):
    # Lets make this object able to accept list of employees as to make this object their supervisor
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # If we do not passed in employees, then it will make self.employees a empty list where we can add employees
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # Make a function to add employees to his/her supervision
    def addEmps(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # Make a function to remove employees
    def delEmps(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # Make a funtion to print all employees fullname
    def printEmps(self):
        print("Under my supervision:")
        for emp in self.employees:
            print("  -->" + emp.fullname())


# Make a manager instance
manager1 = Manager("Harry", "Potter", 10000)
print(manager1.employees)  # We didnt passed in anything so it should be empty

# Lets add the 2 devs to his supervision
manager1.addEmps(dev1)
manager1.addEmps(dev2)

# Then print all of the emps
manager1.printEmps()

# Then remove one emp
manager1.delEmps(dev2)

print()

# Print all emps again
manager1.printEmps()

print()

##Dunder Methods (Magic Methods)
# This are methods that can emulate a built-in behaviour of our instances when you do something to them like adding two instance, or doing things like len(instance)
# Check this code below
print(emp1)

# We can change the output that is produced when you ran that code using dunder methods, so im gonna make a new class identical to our Employee class, but instead, add a dunder method called __str__ and __repr__
# __repr__ - is more of an unambiguous representation of the object/instance itself, it is used more for debugging and logging purposes.
# __str__ - is more of a readable representation of the object/instance and it is meant to be a display to the user
class Employee1(Employee):
    # Im not gonna call init, because we are not gonna add another instance variables

    # Creating __repr__ method
    # The best way to create this method is to make sure that try to display something you can copy and paste back to the python code to create this object
    def __repr__(self):
        return f'Employee1("{self.first}", "{self.last}", {self.pay})'

    # Creating __str__ method
    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    # Making __add__ method to sum up the employees pays
    # self - is for the left side
    # other - right side
    # (emp1 + emp2) , emp1 == self and emp2 == other
    def __add__(self, other):
        return self.pay + other.pay

    # Making len function for the instance's fullname
    def __len__(self):
        return len(self.fullname())


# Make instance of the class
emp1 = Employee1("Hoax", "Snowden", 50000)
print(repr(emp1))  # Shows representation of the class
print(
    emp1
)  # You can just print it because__str__ will be used instead of the __repr__ as __str__ is the last thing in the class

# We can also use __add__, search for https://docs.python.org/3/reference/datamodel.html to see another dunder methods
# Check the dunder add method in our class
emp2 = Employee1("Test", "User", 60000)
emp3 = Employee1("Some", "User", 10000)
print(emp1 + emp2)  # As you can see we can add 2 employees pays but not 3


# We can also use the __len__ to count the length of their full name
# try to comment the __len__ method above then try to use the len on one of the emp to see what happens
print(len(emp1))  # 12
print(len(emp2))

print()

##Property Decorator - We can use a function/method as a property of our class. for example, all of the classes above use a emp1.fullname() to print each employees instance, but we want to use it as emp1.fullname right? in that case we can use the property decorator in the example below

# Just gonna override the class Employee above to help you understand it more
class Employee:

    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + last + "@comp.com", I commented this out bcoz i made a property method below

        Employee.num_of_emps += 1

    """
	def fullname(self):
		return self.first + " " + self.last
	"""

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)

    # Make a property with method
    @property
    def fullname(self):
        return f"{self.first} {self.last}"  # This will print the employees fullname

    # Also use property for our email
    @property
    def email(self):
        return f"{self.first}.{self.last}@comp.com"

    # Make a setter for our fullname
    # It should be propertyname.setter
    # the 'name' in our fullname(self,name) is the string that we will pass in
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")  # Splits name by a whitespace
        self.first = first
        self.last = last

    # Making a deleter if we want to delete its fullname
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


# Make instance of the class
emp1 = Employee("Hoax", "Snowden", 50000)
print(
    emp1.fullname
)  # As you can see, we do not need to put () because it is now a property and not a method anymore
print(emp1.email)  # I also made a property for this email

##Setters and deleters
# If we try to set the full name of our emp1 without the fullname.setter above, it will give us an error and this is where setters can come in
# Now we can run this because we have a setter now
emp1.fullname = "Test User"
print(emp1.fullname)
print(emp1.first)
print(emp1.last)

# Now i made a deleter above just to delete our emp1 fullname
# Delete the fullname of our emp1
del emp1.fullname
print(emp1.fullname)
print(emp1.email)

# Lets add a full name back
emp1.fullname = "Hoax Snowden"
print(emp1.email)
