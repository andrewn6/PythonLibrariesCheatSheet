class Employee:
	
	numofemps = 0
	raise_amt = 1.04
	
	def __init__(self, first, last, age, pay):
		self.first = first
		self.last = last
		self.age = age
		self.email = f"{first}.{last}@company.com"
		self.pay = pay
		
		Employee.numofemps += 1
	
	def showFull(self):
		return f"{self.first} {self.last}"
	
	@classmethod
	def set_raise_amt(cls, amt):
		cls.raise_amt = amt	
				
	@classmethod
	def fromString(cls, empstr):
		first, last, age, pay = empstr.split("-")
		return cls(first, last, age, pay)
	
	@staticmethod
	def isItWorkDay(day):
		if day.lower() == "saturday" or day.lower() == "sunday":
			print("It is not workday")
		else:
			print("It is workday")

		
emp1 = Employee("Hoax","Snowden", 14, 10000)

empstr1 = "Elliot-Alderson-13-1000"
emp2 = Employee.fromString(empstr1)

emp1.set_raise_amt(1.05)

print(emp2.email)
print(Employee.numofemps)
Employee.isItWorkDay("Sunday")

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)	

