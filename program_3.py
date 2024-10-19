# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []
    loop='y'
    while loop=='y':
        list1=input('Enter a year.')
        list2=input('Enter the state you are adding information for in that year.')
        list3=int(input('Enter the population.'))
        list=[list1,list2,list3]
        loop=input('Enter y to add more. Else, press another letter key.')
        all_entered_values.append(list)
    else:
        year_to_sum=input('Please enter a year to see the total population for that year.')
        sum_population_for_year(list3,year_to_sum)
        

    # Now have the user enter a year. 
    
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

def sum_population_for_year(list3, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.
    #year_to_sum=float(input('Please enter a year to see population for that year.'))
    total=0
    for year_to_sum in list:
        total=total+list3
    print(total)

    # print the totalled population
# Call the main function.

if __name__ == '__main__':
    main()
