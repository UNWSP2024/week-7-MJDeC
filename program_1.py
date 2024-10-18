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
    total=0
  for x in rain:  
    total+=x
  print('The total amount of rain over the year was',format(total,'.2f'),'inches.')
  avg=total/12
  print('The average amount of rain per month was',format(avg,'.2f'),'inches.')
  most=max(rain)
  if most==rain[0]:
    monthm='January'
  if most==rain[1]:
    monthm='February'
  if most==rain[2]:
    monthm='March'
  if most==rain[3]:
    monthm='April'
  if most==rain[4]:
    monthm='May'
  if most==rain[5]:
    monthm='June'
  if most==rain[6]:
    monthm='July'
  if most==rain[7]:
    monthm='August'
  if most==rain[8]:
    monthm='September'
  if most==rain[9]:
    monthm='October'
  if most==rain[10]:
    monthm='November'
  if most==rain[11]:
    monthm='December'
  least=min(rain)
  if least==rain[0]:
    monthl='January'
  if least==rain[1]:
    monthl='February'
  if least==rain[2]:
    monthl='March'
  if least==rain[3]:
    monthl='April'
  if least==rain[4]:
    monthl='May'
  if least==rain[5]:
    monthl='June'
  if least==rain[6]:
    monthl='July'
  if least==rain[7]:
    monthl='August'
  if least==rain[8]:
    monthl='September'
  if least==rain[9]:
    monthl='October'
  if least==rain[10]:
    monthl='November'
  if least==rain[11]:
    monthl='December'
  print('The month with the highest amount of rain was',monthm,'.')
  print('The month with the least amount of rain was',monthl,'.')
main()
