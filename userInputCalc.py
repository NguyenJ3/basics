#Get user information

name = input("What is your name ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

radius = float(input("Enter radius of circle: "))


#print greetings

print("Hello, " + name + "!")


#calculations

print("Sum is: ", num1 + num2)

area = 3.14159 * radius ** 2 #pi x radius raised to power of 2 

print ("Area is: ", area)


#concluding answer ELIF statement based on user choice

answer = input("Are you enjoying Python? (yes/no)").lower() #answer yes or no ONLY in lowercase

if answer == " yes":
    print("Nice keep going ")

else:
    print("Don't give up!")




