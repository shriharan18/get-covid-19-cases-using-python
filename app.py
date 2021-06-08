# This code was written by Shreeharan for the YouTube Channel Stark Intelligence
from covid import Covid     # mporting the modules
covid = Covid()             # defining the variable covid
country_name = input('Enter the country name: ')    # geting input from the user
cases = covid.get_status_by_country_name(country_name)  # getting cases
for x in cases:
    print(x,':',cases[x])       # printing cases
