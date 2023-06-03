class Time:
    def __init__(self,hour,minute,second):
        if choice == "1" :
            self.h = hour
            self.m = minute
            self.s = second
            while self.s >= 60:
                self.s -= 60
                self.m +=1
            while self.m >= 60:
                self.m -= 60
                self.h += 1
        elif choice == "2" :
            self.h = 0
            self.m = 0
            self.s = second 
    def show(self):
        print(self.h , ":", self.m , ":", self.s)
    def calculator(self):
        if choice == "1":
            self.s += self.h * 3600 + self.m * 60
            self.m = 0
            self.h = 0    
            self.show()
        elif choice == "2":
            while self.s >= 60 :
                self.s -= 60
                self.m += 1
            while self.m >= 60 :
                self.m -= 60
                self.h += 1
            self.show()
            
            
print("Hello,I'm a time calculator,lets begin")
choice = input("choose your format: hour:minute:second to 0:0:second (Enter 1)/ 0:0:second to hour:minute:second (Enter 2)")

if choice == "1":
    time_h = int(input("Enter Hour: "))
    time_m = int(input("Enter Minute: "))
    time_s = int(input("Enter Second:"))
    time = Time(time_h, time_m, time_s)
elif choice == "2":
    time_s = int(input("Enter Second:"))
    time = Time(0, 0, time_s)
time.show()
time.calculator()