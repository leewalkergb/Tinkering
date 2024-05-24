#
# Created on: Fri May 24 2024
# Last Update: 24/05/24
#
# Author: Lee Walker
# Github: https://github.com/leewalkergb
#
# Filename: magic_8ball.py
# Version: v1.0
# Description: Magic 8-ball exercise on codecademy.
#

#-----------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------
import random

#-----------------------------------------------------------------------
# Variables
#-----------------------------------------------------------------------

name = "Lee"
question = "Is the earth round?"
answer = ""
random_number = random.randint(1,9)

#-----------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------

if random_number == 1:
    answer = "Yes - Definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"
    
print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)