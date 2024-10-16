# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []
    loop='y'
    while loop=='y':
        all_entered_values=input('Enter a year, a state, and a population separated by commas.')
        loop=input('Enter y to add more. Else, press another letter key.')
    else:
        year_to_sum=float(input('Please enter a year to see population for that year.'))
        sum_population_for_year(all_entered_values,year_to_sum)
        

    # Now have the user enter a year. 
    
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year

def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.
    #year_to_sum=float(input('Please enter a year to see population for that year.'))
    total=0
    for all_entered_values[year_to_sum]:
        total=total+all_entered_values
    print(total)

    # print the totalled population
# Call the main function.

if __name__ == '__main__':
    main()
