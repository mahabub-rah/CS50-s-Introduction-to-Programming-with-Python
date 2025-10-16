# Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

# breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.

def main():
    user_time = input('What time is it?: ').lower()
    time = convert(user_time)

    if time >= 7 and time <=8 :
        print('breakfast time')
    elif time >= 12 and time <=13 :
        print('lunch time')
    elif time >= 18 and time <=19 :
        print('dinner time')


def convert(time):
    # for am
    if 'am' in time:
        time = time.replace('am', '').strip()
        hour, minute = time.split(':')
        hour = int(hour)
        if hour == 12:  
            hour = 0
        return hour + int(minute) / 60
    # for pm
    elif 'pm' in time:
        time = time.replace('pm', '').strip()
        hour, minute = time.split(':')
        hour = int(hour)
        if hour != 12:   
            hour += 12
        return hour + int(minute) / 60
    #international time
    else: 
        hour, minute = time.split(':')
        return int(hour) + int(minute) / 60
   

# already call the main function
if __name__ == "__main__":
    main()


