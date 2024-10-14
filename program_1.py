# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.
num_months=12
def main():
  rain=[0]*num_months
  print('Enter the rainfall for each month.')
  for index in range(len(rain)):
    rain[index]=float(input(f'Month {index+1}:'))
    rain_total=rain
    print('The total amount of rain over the year was',rain_total,'inches.')
    

main()
