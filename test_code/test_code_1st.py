import unittest

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, upraise=5000):
        self.salary += upraise


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee1 = Employee('jim', 5000)

    def test_give_default_raise(self):
        self.employee1.give_raise()
        self.assertEqual(self.employee1.salary, 10000)
