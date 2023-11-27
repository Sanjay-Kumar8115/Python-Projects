from datetime import time,date,datetime,timedelta

year=int(input("Enter your DOB(Year) : "))
month=int(input("Enter your DOB(month) : "))
day=int(input("Enter your DOB(day) : "))
curr_date=date.today()
print(curr_date)
date1=datetime(year,month,day,12,00,00)
date2=datetime(curr_date.year,curr_date.month,curr_date.day,3,4,00)
age=date2-date1
print("Your toatl age in days is : ",age)

