# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 
import math
def main():
  first_coords=eval(input('Enter the first set of three coordinates, separated by commas.'))
  second_coords=eval(input('Enter the second set of three coordinates, separated by commas.'))
  #if:
  #print('Please enter valid coords.')
  distance()
  print(mathiness)
  
def distance(first_coords, second_coords):
  first_coords[0]=x1
  first_coords[1]=y1
  first_coords[2]=z1
  second_coords[0]=x2
  second_coords[1]=y2
  second_coords[2]=z2
  mathiness=sqrt((x2-x1)^2 +(y2-y1)^2 +(z1-z2)^2)

main()
