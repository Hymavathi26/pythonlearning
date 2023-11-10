class GF:
    def car(self):
        return "Old car"

class F(GF):
    def car(self):
        return "honda car"

class S(F):
    def car(self):
        return "lambo"

son=S()
print(son.car())       #lambo--> bcoz it takes recent method output when all methods are same
