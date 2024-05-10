#
# Created on: Mon May 06 2024
# Last Update: 
#
# Author: Lee Walker
# Github: https://github.com/leewalkergb
#
# Filename: space.py
# Version: v0.1
# Description: Optional control flow exercise
#
print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:
if planet == 1:
  print("On Venus, Codey's weight will be " + str(weight * 0.91))
elif planet == 2:
  print("On Mars, Codey's weight will be " + str(weight * 0.38))
elif planet == 3:
  print("On Jupiter Codey's weight will be " + str(weight * 2.34))
elif planet == 4:
  print("On Saturn, Codey's weight will be " + str(weight * 1.06))
elif planet == 5:
  print("On Uranus, Codey's weight will be " + str(weight * 0.92))
else:
  print("On Neptune, Codey's weight will be " + str(weight * 1.19))