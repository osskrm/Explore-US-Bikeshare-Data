city = ''
while city not in valid_cities:
    city = input("\nPlease choose a city you would like to see the data for: Chicago, New York City, or Washington?\n").lower()
    if city in valid_cities:
        city = city_map[city]
    else:
        print("Sorry, input city is not in the list!")




total_travel_time = df['Trip Duration'].sum()
print('Total travel time:', total_travel_time / 86400, " Days")

average_travel_time = df['Trip Duration'].mean()
print('Average travel time:', average_travel_time / 60, " Minutes")
