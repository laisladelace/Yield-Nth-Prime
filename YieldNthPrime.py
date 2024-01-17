
############################
# Step 1 = Import libraries
############################

import time 
start = time.time()

###################################
# Step 2 = Define the Function(s) 
###################################
def find_a_list_of_prime_numbers():
    print ('Choose a range (from x through y)')
    ##
    #5:29 pm Tues., 1/16/24, 
    ##It's here where we were stopped. What I am going to try to do is include the notes I have in the original code. 
    x_value = int (input ('Enter x (greater than 1):'))
    y_value = int(input('Enter y:')) 

#We need to initialize, or name and create a space for, an empty list. 
    list_prime_num = []
#Now we need to set up the conditions tha tguide how we build the list from the empty set. 
    ## We use "number" to represent any specific value of n we choose from the range
    ###while remembering that 9n) is the general non-zero or non-single set of 
    ####integers we test within the range of (x_value to y_value +1)

    for number in range (x_value, y_value + 1):
    #We use y_value + 1 to include the last number in the range if it's the 
    ##y+value 
        for n in range (2, number):
            if number%n==0:
                break 
        else: 
            list_prime_num.append(number)
    #What the above block denotes is that ....
    ##f the number itself is actually prime, add the number to the list
    ##to the list of prime numbers that starts with an empty set
    ###By matching the 'else' with the 'for' rather than 'if', we ensure that
    ####the numbers do not repeat in the list. 
    ####The list is also now "correct" because it doesn't only work
    #### if the number is divisible by something other than 1 or itself
            

    #now we will show the result of the list function 
    print ()
    print (f'Prime numbers from{x_value}through{y_value}:')
    for prime in list_prime_num:
            #We will go ahead and print the F string for the prime number
            print (f'{prime},', end = '') 
    print ()

#******************************#
# Step 3 = Execute the Program
#******************************#
find_a_list_of_prime_numbers()

end = time.time()
print(f"The total run time for the program was:")
print (round(end-start,2),"seconds")

#******************************************************************************************************************#
###Not gonna approach the graphing at this time as I'm trying to determine the bug in the first part of the project 
#******************************************************************************************************************#


'''


##################
# Import libraries
##################

import time

##################
# Define functions
##################

def find_a_list_of_prime_numbers(nPrimes):

    # Initialize an empty list
    list_prime_num = []

    # First loop: iterate through indeces
    for idx in range(1, nPrimes +1):

        print(f"Index: {idx}")

        # Second loop: for each index, check if the number is prime
        for n in range(2, idx):

            print(n)

            if idx % n == 0:
                print("yolo")
                break

            else: 
                print("nolo")
                list_prime_num.append(idx)

#        print(idx)
#        print(list_prime_num)

#    print(f"Prime numbers between {x_value} and {y_value} are:")
#    for prime in list_prime_num:
#        print(f'{prime}', end = '\n')

###########
# Execution
###########

# - Start the timer
start = time.time()

# - This is where you actually run the function
find_a_list_of_prime_numbers(10)

# - End the timer
end = time.time()

# - Print run time
print (f"The total run time for the program was: {round(end-start,4)}")




#Okay, now for the graphing part 

#Make a graph of all the prime numbers from 2 to 97 as well as a graph for how long the program took to run 



#Start timing the program 
start = time.time()

#Define the program 
def find_a_list_of_prime_numbers():
    print ('Choose a range (from x through y)')
    x_value = 2
    y_value = 100

    list_prime_num = []
    for number in range(x_value, y_value + 1): 
        for n in range(2, number):
            if number %n==0:
                break 
        else: 
            list_prime_num.append(number)
    print ()
    print(f'Prime numbers from {x_value} through {y_value}:')
    for prime in list_prime_num:
        print(f'{prime},', end = '')
    print ()

#Run the program 
find_a_list_of_prime_numbers()

#End the timing of the program 
end = time.time()
print (f"The total run time for the program was:")
print (round(end-start,2),"seconds")
       
#Set up the graph     
import matplotlib.pyplot as plt
#I know I cheated to get the quick fix; I have the list of the prime numbers from 1 to 100 memorized....
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#Plot the graph 
plt.plot(x,y)
plt.xlabel('The Value of N')
plt.ylabel('The Nth Prime Number')
plt.title('The Prime Numbers from 2 to 97')
plt.show()

'''