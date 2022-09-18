Year = int(input("Enter the number: "))

digits = len(str(Year))

if digits < 4:
  print("Year should be in four digit")
  SystemExit(0)
elif((Year % 400 == 0) or
     (Year % 100 != 0) and
     (Year % 4 == 0)):
    print("Given Year is a leap Year");
else:
    print ("Given Year is not a leap Year")