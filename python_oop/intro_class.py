# python object-oriented programming

class Employee:

  num_employees = 0
  raise_amount = 0.03   # class variable

  # constructor
  def __init__(self, first, last, pay):
    self.first = first  # instance variable
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'
    Employee.num_employees += 1 # reference class's attribute

  # regular methods in class
  def fullname(self):
    return self.first + ' ' + self.last

  def apply_raise(self):
    self.pay = int(self.pay * (1 + self.raise_amount))

  # class method
  @classmethod
  def set_raise_amt(cls, amount):
    cls.raise_amount = amount

  # class-method style constructor
  @classmethod
  def from_string(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)

  # static method
  @staticmethod
  def is_workday(day):
    if day.weekday() == 5 or day.weekday() == 6:
      return False
    return true

emp_1 = Employee('Hao', 'Wang', 160000)
emp_2 = Employee('Bonzi', 'Wang', 120000)

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(Employee.fullname(emp_1)) # explicitly pass the instance
print(emp_1.fullname())

print(Employee.__dict__)
print(emp_1.__dict__)       # not seeing raise_amount

Employee.raise_amount = 0.05    # aplly on class's attribute
emp_1.raise_amount = 0.10       # apply on instance's attribute

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.set_raise_amt(0.08)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_3 = Employee.from_string('Steve-Smith-30000')
print(emp_3.email)

import datetime
my_date = datetime.date(2017, 8, 27)
print(Employee.is_workday(my_date))

