#
# Created on: Fri May 24 2024
# Last Update: 24/05/24
#
# Author: Lee Walker
# Github: https://github.com/leewalkergb
#
# Filename: shipping.py
# Version: v1.0
# Description: Sal's Shipping codecademy task
#

#-----------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
# Variables
#-----------------------------------------------------------------------
weight = 80
ground_premium = 125.00
flat_charge = 20
method = ""

#-----------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------
# Ground Shipping Calculation
if (weight <= 2):
    cost_ground = (weight * 1.25) + flat_charge
elif (weight > 2) and (weight <= 6):
    cost_ground = (weight * 3.00) + flat_charge
elif (weight > 6) and (weight <= 10):
    cost_ground = (weight * 4.00) + flat_charge
elif (weight > 10):
    cost_ground = (weight * 4.75) + flat_charge
else:
    cost_ground = "Error"

# Need to do this formatiing to get two decimal places if the second is a 0. Need to convert to string otherwise a type error
# print("Ground shipping cost $", str('%.2f' % cost_ground)) 
# print("Ground Shipping premium cost $", str('%.2f' % ground_premium))

# Drone Shipping Calculation
if weight <= 2:
    cost_drone = weight * 4.5
elif weight > 2 and weight <= 6:
    cost_drone = weight * 9.0
elif weight > 6 and weight <= 10:
    cost_drone = weight * 12.00
elif weight > 10:
    cost_drone = weight * 14.25
else:
    cost_drone = "Error"

# Need to do this formatiing to get two decimal places if the second is a 0. Need to convert to string otherwise a type error
print("Ground shipping cost $", str('%.2f' % cost_ground)) 
print("Ground Shipping premium cost $", str('%.2f' % ground_premium))
print("Drone shipping cost $", str('%.2f' % cost_drone))