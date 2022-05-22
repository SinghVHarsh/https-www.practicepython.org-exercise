from datetime import date
today_date=date.today()
name = input("enter the name: ")
age = int(input("enter the age: "))
exp = "You will attain the age of 100 years on "+(str(int(today_date.year)+100-age)+'\n')
num = int(input("enter the number of statements:"))
print(exp*num)


