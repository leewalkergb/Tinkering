#
# Created on: Sat Apr 27 2024
# Last Update: 
#
# Author: Lee Walker
# Github: https://github.com/leewalkergb
#
# Filename: lovely_loveseats.py
# Version: v0.1
# Description: Lovely loveseats codecademy task
#

#------------------------------------------------------------
# Variables
#------------------------------------------------------------

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

sales_tax = 0.088

customer_one_total = 0
customer_one_itemization = ""

# Add Customer One Items
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization = (customer_one_itemization + " \n" + luxurious_lamp_description)

# Calculate Customer One Total incl. Tax
customer_one_tax = (customer_one_total * sales_tax)
customer_one_total += customer_one_tax

# Receipt Printing
print("Customer One Items: ")
print(customer_one_itemization)
print("Customer One Total: ")
print(round(customer_one_total, 2))