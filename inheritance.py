class A:
    def m1(self):
        print('m1 of a class A')
    def m2(self):
        print('m2 of a class A')
class B(A):
    def m3(self):
        print('m3 of class B')
    def m4(self):
        print('m4 of class B')
    def m1(self):
        print('m1 of B class')
obj=B(A);
obj.m1()
    
        