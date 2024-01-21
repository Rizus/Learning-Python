# main.py
from mypackage.module1 import greet
from mypackage.subpackage.module3 import people

for person in people:
    greet(person)
    