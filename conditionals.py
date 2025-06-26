#Get user to give a number between 0-100 and if pass x >  60 otherwise fail

grade = int(input("What is your grade?:  "))

#elif statements, check if grade is over 60 or else print "Fail"

if grade >= 60 :
    print("Pass!")
else:
    print("Fail")


#temperature check ask user for temperature 
temp =  int(input("What temperature is it?: "))

#elif statement if below 50 print "Cold" if between 80 and 50 print "warm" over 80 prints "hot"

if temp < 50:
    print("Cold")

elif 50 < temp < 80:
    print("Warm")

else:
    print("Hot")