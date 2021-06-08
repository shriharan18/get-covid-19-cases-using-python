from covid import Covid
covid = Covid()
country_name = input('Enter the country name: ')
cases = covid.get_status_by_country_name(country_name)
for x in cases:
    print(x,':',cases[x])