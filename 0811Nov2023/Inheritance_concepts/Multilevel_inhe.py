#Multilevel Inheritance
#Grandfather-father-Son

class GrandParant:
    def grandparent_method(self):
        return "Grandparent's method"

class Parent(GrandParant):
    def Parent_method(self):
        return "Parent's method"

class Child(Parent):
    def child_metyhod(self):
        return "Child's method"

child=Child()                   #using child class obj invoke GF and Parent class methods
print(child.grandparent_method())
print(child.Parent_method())
print(child.child_metyhod())

