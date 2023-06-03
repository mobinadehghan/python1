class Date:
    def __init__(self, year, month, day):
        self.y = year
        self.m= month
        self.d= day
        
        
#chon 6 mah aval 31 rooze v 6 mahe dovom 30 rooze hastand
    def show(self):
        print(self.y, "/",self.m, "/",self.d)
            
            
            
    def validate(self):
        if self.m <= 6:
            while (self.y <= 0 or self.y >= 10000) or (self.m <= 0 or self.m >= 7 ) or (self.d >= 32 or self.d <= 0):
                print("Invalid Date,RE-enter Date,Remember:If your month is between 1 and 6,day can be assigned 31")
                self.y = int(input("Re-enter Year: "))
                self.m = int(input("Re-enter Month: "))
                self.d = int(input("RE-enter Day: "))
        elif self.m > 6:
            while (self.y <= 0 or self.y >= 10000) or (self.m <= 6 or self.m >= 13 ) or (self.d >= 31 or self.d <= 0):
                print("Invalid Date,RE-enter Date,Remember:If your Month is between 6 and 12,day can not be assigned 31")
                self.y = int(input("Re-enter Year: "))
                self.m = int(input("Re-enter Month: "))
                self.d = int(input("RE-enter Day: "))
        print("Your date is entered correctly and it is validated.")
        self.show()
            
            
    def get_month(self):
        months = ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar", "Mehr", "Aban", "Azar", "Day", "Bahman", "Esfand"]
        for i in range(len(months)+2):
            if self.m == (i) :
                print(self.y, "/",months[i-1], "/", self.d)
                    
                    
    def sum(self,second_date):
        sum = Date(None, None, None)
        sum.y = self.y + second_date.y
        sum.m = self.m + second_date.m
        sum.d = self.d + second_date.d
        print("Month will be considered to have 30 days")
        while sum.d > 30:
            sum.d -= 30
            sum.m += 1
        while sum.m > 12:
            sum.m -= 1
            sum.y += 1
        sum.show()
            
    def subt(self,second_date):
        if (self.y * 365 + self.m * 30 + self.d) > (second_date.y * 365 + second_date.m * 30 + second_date.d):
            sub = Date(None, None, None)
            sub.y = self.y - second_date.y
            sub.m = self.m - second_date.m
            sub.d = self.d - second_date.d
            #mabaghi sharayet dar tabe e Validation hal mishe,mesle month>12 ya day>30.
            while sub.m < 0 :
                sub.m += 30
                sub.y -= 1
            while sub.d < 0 :
                sub.d += 30
                sub.m -= 1
            sub.show()
        elif (second_date.y * 365 + second_date.m * 30 + second_date.d) > (self.y * 365 + self.m * 30 + self.d):
            sub = Date(None, None, None)
            sub.y = second_date.y - self.y
            sub.m = second_date.m - self.m
            sub.d = second_date.d - self.d
            if sub.m < 0 :
                sub.m += 30
                sub.y -= 1
            if sub.d < 0 :
                sub.d += 30
                sub.m -= 1
            sub.show()
date_one_year = int(input("Enter your first Date Year,Remember: 0 < Year < 10000 : "))
date_one_month = int(input("Enter your first Date Month,Remember: 0 < Month < 13 : "))
date_one_day = int(input("Enter your first Date Day,Remember: 0 < Day < 32 if 0 < Month <7, or 0 < Day < 31 if 6 < Month < 13 : "))
first_date = Date(date_one_year, date_one_month, date_one_day)
first_date.validate()
date_two_year = int(input("Enter your first Date Year,Remember: 0 < Year < 10000 : "))
date_two_month =int(input("Enter your second Date Month,Remember: 0 < Month < 13 : "))
date_two_day = int(input("Enter your second Date Day,Remember: 0 < Day < 32 if 0 < Month <7, or 0 < Day < 31 if 6 < Month < 13 : "))
second_date = Date(date_two_year, date_two_month, date_two_day)
second_date.validate()
first_date.get_month()
second_date.get_month()
first_date.sum(second_date)
first_date.subt(second_date)