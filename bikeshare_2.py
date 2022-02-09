import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    city = input("What is the city name (chicago , new york city , washington) ?").lower()
    while city not in CITY_DATA.keys():
        print("Invalid City")
        city = input("What is the city name (chicago , new york city , washington) ?").lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input("What is the month (january , february , march , april , may , june , all) ?").lower()
    while month not in months:
        print("Invalid Month")
        month = input("What is the month (january , february , march , april , may , june , all) ?").lower()
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    day = input(
        "What is the day (saturday , sunday , monday , tuesday , wednesday , thursday , friday , all) ?").lower()
    while day not in days:
        print("Invalid Day")
        day = input(
            "What is the day (saturday , sunday , monday , tuesday , wednesday , thursday , friday , all) ?").lower()

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print("The most common month is : {}".format(df['month'].mode()[0]))
    print("The most common day of week is : {}".format(df['day_of_week'].mode()[0]))
    print("The most common start hour is : {}".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("The most common start station is : {}".format(df['Start Station'].mode()[0]))

    print("The most common end station is : {}".format(df['End Station'].mode()[0]))

    df['combination_trip'] = df['Start Station'] + " , " + df['End Station']
    print("The most common start station and end station are : {}".format(df['combination_trip'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print("The total travel time is : {}".format(df['Trip Duration'].sum()))
    print("The mean travel time is : {}".format(df['Trip Duration'].mean()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print(" counts of user types : {}".format(df['User Type'].value_counts()))

    if city != 'washington':
        print("counts of gender is : {}".format(df['Gender'].value_counts()))
        print('The most common year of birth is {} '.format(df['Birth Year'].mode()[0]))
        print("The max year of birth is {}".format(df['Birth Year'].max()))
        print("The min year of birth is {}".format(df['Birth Year'].min()))
    else:
        print("Sorry !!  There aren't information about gender and birth year in washington")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    counter = 0
    bol = ['yes', 'no']
    user = input("would you like to display 5 rows from data , please type (yes or no)").lower()
    if user not in bol:
        print("Invalid input , please type (yes or no) ")
        user = input("would you like to display 5 rows from data , please type (yes or no)").lower()
    elif user == 'no':
        print("thank you")
    else:
        while counter + 5 < df.shape[0]:
            print(df.iloc[counter:counter + 5])
            counter += 5
            user = input("would you like to display 5 rows from data , please type (yes or no)").lower()
            if user == 'no':
                print("thank you")
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()