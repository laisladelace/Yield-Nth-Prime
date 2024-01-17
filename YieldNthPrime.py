#*********************#
#ControlledExperiment   1/16/24 5:03 pm PT
#*********************#

#Project Objective: Make a graph of all the prime numbers from 2 to 98 as well as a graph for how long the program took to run 

#Problem: code doesn't work in visual studio code on the PC or MAC
#Hypothesis: it's either the code or the program and if I change one of those things, then things should work because there aren't any glitches 
##independent variable(s) to test = which computer I use to run the code; which platform; specific code I use; typing everything in myself into the computer rather than copy and paste from iPad
###another problem is how do I test the program? 



#**************************#
# Step 1 = Import libraries
#**************************#

import time 
start = time.time()

#********************************#
# Step 2 = Define the Function(s) 
#********************************#

def find_a_list_of_prime_numbers():
    print ('Choose a range (from x through y)')
    x_value = 2
    y_value = 100 

    list_prime_num = []
    for number in range (x_value, y_value + 1):
        for n in range (2, number):
            if number%n==0:
                break 
        else: 
            list_prime_num.append(number)
    print ()
    #rn I'm keeping the extra prints just to keep the experiment controlled#
    print (f'Prime numbers from {x_value} through {y_value}:')
    for prime in list_prime_num:
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

#Seeing yolo made me laugh AGAIN haha <3




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


"""
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

#Set up another graph 
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
y = #This is where I'm stuck. I don't even know what to Google on how to search for how to do this lol but I'll get to this part tomorrow. 
