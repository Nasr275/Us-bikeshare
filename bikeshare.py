import time
import pandas as pd
import numpy as np
DAYS= ['all','monday','tuesday','wendesday','thuresday','friday','saturday','sunday']
MONTHS = ['all','january', 'february', 'march',
          'april', 'may', 'june']
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid = True
    while valid:        
        city = input('Enter a city name : ').lower()
        if city in CITY_DATA :
            
            print('Thanks, one moment while we process the data')
            valid = False # To Exit the loop     
        else:
            
            print('sorry invalid city try again')
                
    # TO DO: get user input for month (all, january, february, ... , june)
    valid = True
    while valid:
        
        month = input('Please enter a month name : ').lower()
        if (month in MONTHS):           
            print('Thanks, one moment while we process the data')
            valid = False # To Exit the loop     
        else:           
            print('{} is an invalid month you should choose between january and june'.format(month))
    
            
            
         

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid = True
    while valid:
        
        day = input('Please enter a day name : ').lower()                              
        if day in DAYS:
            print('Thanks, one moment while we process the data')
            valid=False
        else:
            print('sorry invalid day name try again')
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city]) 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()  # A different function is used because the function used in the tutorial has been deprecated

    if month != 'all':
       
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':        
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()
    print('The most common month is : ',common_month)
    
    # TO DO: display the most common day of week
    df['day_name'] = df['Start Time'].dt.day
    common_day = df['day_name'].mode()
    print('The most common day is : ',common_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()
    print('The most common start hour is : ',common_hour)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()
    print('The most common start station is : '+common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()
    print('The most common End station is : '+common_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    frequent_stations = df.groupby(['Start Station'])['End Station'].size().nlargest(1)
    print('Most frequent start and end station: ', frequent_stations)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time and display mean travel time
    if ('Trip Duration' in df.columns):
        
        total_time = df['Trip Duration'].sum()
        print('The total travel time is : {} seconds'.format(total_time))
        mean_time= df['Trip Duration'].mean()
        print('The average travel time is : {} seconds'.format(mean_time))
    else:
        print('The trip duration is not specified in this city research data')
    # TO DO: display mean travel time
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print('The number of unique user types are ' , user_types)

    # TO DO: Display counts of gender
    if ('Gender' in df.columns ):                                                    
        count_gender = df['Gender'].value_counts()
        print('The number of males and females is ' , count_gender) 
    else:
        print('Gender is not specified in this city research data')
    # TO DO: Display earliest, most recent, and most common year of birth
   
    if ('Birth Year' in df.columns):
            
        earlist_date = df['Birth Year'].min() #the least recent date
        recent_date = df['Birth Year'].max() #the most recent recent date
        most_common_date = df['Birth Year'].mode() # The most common date
        print('The Earlist , The most recent and the most common years of births are {}, {}, {} respectively '   .format(earlist_date,recent_date,most_common_date))
    else:
            print('Birth year is not specified in this city research data')
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
    

def Display_raw_data(df,city): # A function I added to display raw data 
    
    data = pd.read_csv(CITY_DATA[city])
    user_input=input('Wolud you like to see the first five rows of raw data :').lower()
    valid=True   
    i = 5
    while valid:
        
        
        if(user_input=='yes'):
            print(data.head(i))            
            i+=5 
            user_input=input('Wolud you like to see five more rows :').lower()
        elif (user_input == 'no'):
             valid=False
        else:
            print('Invalid input please try again')
            user_input=input('Wolud you like to see five more rows :').lower()    
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        Display_raw_data(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
