#loop from 1 to 10 using for loop

for i in range(1,11):
    print(i) #prints out current value of i 


#initialize num as 2

num = 2

#while num is less than or equal to 20
while num <=  20: 
    print(num) #print current val of num
    num += 2 #add 2 to print even values 


#Ask user for starting number 

n  = int(input("Enter a number: "))

#countdown loop from n to 0 
while n >= 0: 
    print(n) #prints n while still greater than 0 

    n -= 1 #decreases val of n each time 

    

#print a multiplication table (1 to 10 )
for i in range(1,11): #outer loop for 1 to 10
    for j in range (1,11): #inner loop for 1 to 10 
        print(f"{i} x {j} = {i*j}") #prints mulitplication results 
    print() # prints a blank space after each row 