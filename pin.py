#number of tries 
tries =  0 
#userinput must match the following pin 

correctPin =  "3014489"

enteredPin = (input("Enter your pin!"))


confirmation =  "Yes"


#checks if enterpin is not correctpin then prints that is not correct 
if enteredPin != correctPin:

    print("That is not correct")
#if the pin isnt correct prints out a hint message that converts text to lower 
    decision = (input("Would you like a hint ").lower())

    if decision == confirmation.lower():
       print("Okay give a moment")

    #checks length of string and compares whether or not pin is the same length     
    if len(correctPin) == len(enteredPin):
      print("They are the same length!")


    else: 
       print("The lenght of pin is wrong!")


else:
   print("Success!!")






        
       

    

