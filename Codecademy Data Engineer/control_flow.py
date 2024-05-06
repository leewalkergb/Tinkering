#
# Created on: Mon May 06 2024
# Last Update: 
#
# Author: Lee Walker
# Github: https://github.com/leewalkergb
#
# Filename: control_flow.py
# Version: v0.1
# Description: Notes on control flow
#

# booleans
my_baby_bool = "true"
print(type(my_baby_bool))

my_baby_bool_two = True
print(type(my_baby_bool_two))

# relational operators
# 3*2 != 7 this returns true as 6 does not equal 7
# 4 == 2+2 this returns true as 4 = 4
# Things such as > < <= >= fall into this category as well

# Conditional Statements
# Enter a user name here, make sure to make it a string
user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")

# Boolean Operators
# when using and both must be true
# when using or either can be true
# when using not you have true for every condition but the expression
# not (4+2) -  note that not comes before the expression

#if statements
number =  24

if number != 24:
  print("That is not my number")
else:
  print("You guessed correctly") 

