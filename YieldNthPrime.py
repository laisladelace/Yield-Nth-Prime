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

