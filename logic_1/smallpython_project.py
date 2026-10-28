import random #this is a "library" it gives you more functions like random numbers. it is not used currently.

print ("Even or Odd\n") #tells about porject
while True: #Constantly runs the code below
    number = int(input("Pick a number: ")) #asks for input


    def check_even_or_odd(): #This function allows this "block" of code to be repeated
        if number % 2 == 0: # this is an if statement
            print("Your number is even!") #output if even
        else:
            print("Your number is odd!") #output if odd
    check_even_or_odd() #Call the function