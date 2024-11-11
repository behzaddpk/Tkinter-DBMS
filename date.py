date = int(input("Enter your birthday date: "))
month = int(input("Enter your birthday Month: "))
if month == 1:
    month = "january"

elif month == 2:
    month = "February"

elif month == 3:
    month = "March"

elif month == 4:
    month = "April"
    print("April")
elif month == 5:
    month = "May"

elif month == 6:
    month = "June"

elif month == 7:
    month = "July"

elif month == 8:
    month = "August"

elif month == 9:
    month = "September"

elif month == 10:
    month = "October"

elif month == 11:
    month = "November"

elif month == 12:
    month = "December"
    


year =  int(input("Enter your birthday Year: "))

birthday = str(date) + "," + str(month) + ","  + str(year)



print ("Your birthday is " + str(birthday))