# Question 1: Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function. 
# The first line of the code has been defined as below.

# def hello_name(user_name):
#     # I took the all caps username in the question literally and added .upper()
#     print('hello_'+user_name.upper()+'!')

# hello_name(input("enter your name: "))


# Question 2: Write a python function, first_odds that prints 
# the odd numbers from 1-100 and returns nothing

# def first_odds():
#     for i in range(1,100,2):
#         print(i)

# first_odds()

# Question 3: Please write a Python function, max_num_in_list to return 
# the max number of a given list. The first line of the code has 
# been defined as below.

# def max_num_in_list(a_list):
#     return max(a_list)

# # creating an empty list
# number_list=[]

# # generating numbers 0-50 for the list 
# for i in range(0,51):
#     number_list.append(i)

# # passing the list to the function and printing the results
# print(max_num_in_list(number_list))

# Question 4: Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also 
# divisible by 400. The return should be boolean Type (true/false).

# def is_leap_year(a_year):
    
#     # Creates a variable to hold the inputted year as an int
#     a_year_int = int(a_year)

#     # Checks to see if the year ends with two zeros and is also divisible by 400
#     if a_year_int % 400 ==0:
#         leap = True
#         return leap
            
#     # checks to see if the year is divisible by 4 but not 100
#     elif a_year_int % 4 == 0 and a_year_int % 100 != 0:
#         leap = True
#         return leap
        
#    # all other years are false   
#     else:
#         leap = False
#         return leap
        
# given_year = input('enter a year: ')

# print(is_leap_year(given_year))

# Question 5: Write a function to check to see if all numbers in 
# list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive 
# numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):

    a_list_low = a_list[0]
    a_list_high = a_list[-1] +1
    comp_list = list(range(a_list_low,a_list_high))

    if a_list == comp_list:
        consecutive = True
        return consecutive
    else:
        consecutive = False
        return consecutive


num_list = [21,22,23,24,25,27]

print(is_consecutive(num_list))


    