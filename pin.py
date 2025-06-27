
#userinput must match the following pin 

correctPin =  "3014489"

enteredPin = (input("Enter your pin!"))

confirmation =  ("Yes").lower()


if enteredPin != correctPin:

    print("That is not correct")

    decision = print(input("Would you like a hint ").lower())

    if decision == confirmation:
       print("Okay give a moment")
        
    if len(correctPin) == len(enteredPin):
      print("They are the same length!")


    else: 
       print("The lenght of pin is wrong!")
            
        
        
        #decision == (confirmation):
           # len(correctPin) == len(enteredPin)
           # print("length of password is correct")
         
        #else:
            #print("it is the wrong length")


#else:
   #print("Success!!")






        
       

    

