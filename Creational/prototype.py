# creating a clone of already existing class and then changing the properties of it

from builder import *

print("House 1 \n", house1)

house1Clone = house1

house1Clone.addGarage()

print("house1Clone : ", house1Clone)
