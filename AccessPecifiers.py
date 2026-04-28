class Parents:
    def __init__(self):
        self.public_var = "i am Public"          #creating variable as is public
        self._protected_var = "i am Protected"   #variable with '_' is protected
        self.__private_var = "i am Private"      #variable with  '__' is private

    def access_from_same_class(self):
        print("Inside Parent class: ")
        print("Public : ",self.public_var)
        print("Protected : ",self._protected_var)
        print("Private :",self.__private_var)

class  Child(Parents):
    def access_from_subclass(self):
        print("Inside Child class (Subclass) :")
        print("Public :",self.public_var)
        print("Protected :",self._protected_var)
        try:                                            #we using try to avoid error because we can
            print("Private :",self.__private_var)       #not use private variable in subclass
        except AttributeError:
            print("Private : cannot access (AttributeError)")

class Stranger:

    def access_from_other_class(self,obj):
        print("Inside Stranger class (Unrelated): ")
        print("Public :", obj.public_var)
        print("Protected :", obj._protected_var) #not Recommended
        try:
            print("Private :", obj._Parents__private_var) #we can access private variable using NAME MANAEGLING
        except AttributeError:
            print("Private : cannot access (AttributeError)")


P = Parents()
C = Child()
S = Stranger()

P.access_from_same_class()
C.access_from_subclass()
S.access_from_other_class(P)
