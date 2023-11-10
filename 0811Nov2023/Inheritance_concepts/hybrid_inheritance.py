#Hybrid inhe--
#Combination of multiple types of inheritance, such as single,multi level and multiple inheritance

class A:
    def Method_A(self):
        return "Method A"

class B(A):
    def Method_B(self):
        return "Method B"

class C(A):
    def Method_c(self):
        return "Method c"

class D(B,C):
    def Method_D(self):
        return "Method D"

d=D()
print(d.Method_A())
print(d.Method_B())
print(d.Method_c())
print(d.Method_D())

