class Fraction:
    def __init__(self, soorat, makhraj):
        self.soorat = soorat
        self.makhraj = makhraj

    
    def show(self):
        print(self.soorat, "/", self.makhraj)
        
 #defining + , - , X , /       
    def sum(self, second_fraction):
        sum = Fraction
        sum.soorat = (self.soorat * second_fraction.makhraj) + (second_fraction.soorat * self.makhraj)
        sum.makhraj = self.makhraj * second_fraction.makhraj
        return sum


    def subt(self,second_fraction):
        subtraction = Fraction(None,None)
        subtraction.soorat = (self.soorat * second_fraction.makhraj) - (second_fraction.soorat * self.makhraj)
        subtraction.makhraj = self.makhraj * second_fraction.makhraj
        return subtraction

    def mult(self, second_fraction):
        result = Fraction(None, None)
        result.soorat = self.soorat * second_fraction.soorat
        result.makhraj = self.makhraj * second_fraction.makhraj
        return result
    def division(self, second_fraction):
        division = Fraction(None, None)
        
        
        while second_fraction.soorat == 0 :
            print("Wrong values!Your second fraction must not contain 0 either in  numerator nor denominator.")
            second_fraction.soorat = float(input("Enter numerator again: "))
            
            
        division.soorat = self.soorat * second_fraction.makhraj
        division.makhraj = self.makhraj * second_fraction.soorat
        return division
    
    
while True:
    print("Enter calculation or no?")
    in_or_out=input("(y)/(n)? ")
    if in_or_out == "n":
        break
    print("Welcome to Fraction calculator, Firstly enter your first Fraction, then enter your seonc Fraction, and finally which operation you want.")
    first_fraction = Fraction(None, None)
    first_fraction.soorat = float(input("Enter first fraction numenator: "))
    first_fraction.makhraj = float(input("Enter first fraction denominator: "))
    second_fraction = Fraction(None, None)
    second_fraction.soorat = float(input("Enter second fraction numenator: "))
    second_fraction.makhraj = float(input("Enter first fraction denominator: "))
    while first_fraction.makhraj == 0 or second_fraction.makhraj == 0:
        if first_fraction.makhraj == 0:
            print("Wrong valuess! Your first fraction denominator must not be 0.")
            first_fraction.makhraj = float(input("Enter demoniator again: "))
        if second_fraction.makhraj == 0:
            print("Wrong valuess! Your second fraction denominator must not be 0.")
            second_fraction.makhraj = float(input("Enter demoniator again: "))
    first_fraction.show()
    second_fraction.show()
    choice = input("Which operation you would like to have? (+), (-), (*), (/)? ")
    if choice == "+":
        result = first_fraction.sum(second_fraction)
    elif choice == "-":
        result = first_fraction.subt(second_fraction)
    elif choice == "*":
        result = first_fraction.mult(second_fraction)
    elif choice == "/":
        result = first_fraction.division(second_fraction)
    result.show()