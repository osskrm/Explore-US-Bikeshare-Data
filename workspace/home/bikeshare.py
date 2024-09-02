import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHi! Let\'s explore some US bikeshare data!')

    # Define valid cities, months, and days
    valid_cities = ['new york city', 'nyc', 'new york', 'chicago', 'washington']
    city_map = {
        'new york city': 'New York City',
        'nyc': 'New York City',
        'new york': 'New York City',
        'chicago': 'Chicago',
        'washington': 'Washington'
    }
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    valid_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

    # Get user input for city
    while True:
        city = input("\nPlease choose a city you would like to see the data for: Chicago, New York City, or Washington?\n").lower()
        if city in valid_cities:
            city = city_map[city]
            break
        else:
            print("Sorry, input city is not in the list!")

    # Get user input for month
    while True:
        month = input("\nPlease choose a month you would like to see the data for: January, February, March, April, May, June or type 'all' \n").lower()
        if month in valid_months:
            month = month.title()
            break
        else:
            print("Sorry, invalid input!")

    # Get user input for day
    while True:
        day = input("\nPlease choose a day you would like to see the data for: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' \n").lower()
        if day in valid_days:
            day = day.title()
            break
        else:
            print("Sorry, invalid input!")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nPopular times of travel...\n')
    start_time = time.time()

    # Display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # Display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', popular_day)

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nPopular stations and trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most common start station:', Start_Station)

    # Display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost common end station:', End_Station)

    # Display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('\nMost common trip from start to end:', Combination_Station)

    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nTrip Duration...\n')
    start_time = time.time()

    # Display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print('Total travel time:', Total_Travel_Time / 86400, " Days")

    # Display Average travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Average travel time:', Mean_Travel_Time / 60, " Minutes")

    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nUser info...\n')
    start_time = time.time()

    # Display counts of each user type
    user_types = df['User Type'].value_counts()
    print('Counts of each user type:\n', user_types)

    # Display counts of each gender
    try:
        gender_types = df['Gender'].value_counts()
        print('\nCounts of each gender:\n', gender_types)
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")

    # Display earliest, most recent, and most common year of birth
    try:
        Earliest_Year = df['Birth Year'].min()
        print('\nEarliest Year:', Earliest_Year)
    except KeyError:
        print("\nEarliest Year:\nNo data available for this month.")

    try:
        Most_Recent_Year = df['Birth Year'].max()
        print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
        print("\nMost Recent Year:\nNo data available for this month.")

    try:
        Most_Common_Year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
        print("\nMost Common Year:\nNo data available for this month.")

    print('-'*40)

def display_rows(df):
    """Displays 5 rows based on the choice of the user"""

    i = 0
    user_choice = input("Would you like to see 5 lines of row data? Please type yes or no.").lower()
    if user_choice == 'y' or user_choice == 'yes':
        print("The first five rows of the dataset are: \n",df[i:i+5])
        user_choice = input("\nWould you like to see 5 lines of row of data? Please type yes or no.").lower()

        while user_choice == 'y' or user_choice == 'yes':
            i += 5
            print("\n The next five rows are: ", df[i:i+5])
            user_choice = input("\nWould you like to see 5 lines of row data? Please type yes or no.").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rows(df)

        restart = input('\nWould you like to restart? Type yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()