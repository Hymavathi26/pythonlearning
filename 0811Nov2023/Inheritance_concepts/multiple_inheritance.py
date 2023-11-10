#one child have multiple parents

class Father:
    def father_money(self):
        return "5"

class Mother:
    def mother_money(self):
        return "10"

class Daughter(Father,Mother):
    def child_money(self):
        pass

daughter=Daughter()
print(daughter.father_money())
print(daughter.mother_money())