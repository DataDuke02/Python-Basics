#method overwriting & overloading

class Dad:

    def house(self):
        print("White house")
"""        
    def house(int a , int b): #creating multiple function in same name called overloading
        
    def house(string A):

o = Dad()
o.house ("hi")
"""
class Son(Dad):

    def factory(self):
        print("factory")

    def house(self):            #overwriting the function of parent cls
        print("Yellow house")

S = Son()
S.house()
S.factory()
