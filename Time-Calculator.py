def add_time(start, duration, day_of_week = ''):

    new_time = []
    #breakdown of start time in hours and minutes
    start_hours = int(start.split()[0].split(':')[0])
    start_minutes = int(start.split()[0].split(':')[1])

    #breakdown of time to add
    add_hours = int(duration.split(':')[0])
    add_minutes = int(duration.split(':')[1])

    #assigning AM or PM to string and converting to military time
    day_split = start.split()[1]
    if day_split == 'AM' and start_hours == 12:
        start_hours = 0
    elif day_split == 'PM' and start_hours != 12:
        start_hours += 12
    
    new_hours = start_hours + add_hours
    new_minutes = start_minutes + add_minutes
    if new_minutes >= 60:
        new_hours += new_minutes // 60
        new_minutes = new_minutes % 60

    #calculate No. of days 
    number_of_days = 0
    if new_hours >= 24:
        number_of_days = new_hours // 24
        new_hours = new_hours % 24

    if new_hours > 12:
        new_hours -= 12
        day_split = "PM"
    elif new_hours == 12:
        day_split = "PM"
    elif new_hours == 0:
        new_hours += 12
        day_split = "AM"
    elif new_hours < 12:
        day_split = "AM"
    
    new_time.append(f'{new_hours}:{new_minutes:02d} {day_split}')
    #if a day of the week is given, calculate and add to return string
    if day_of_week:
        days_of_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        new_day = days_of_week.index(day_of_week.lower()) + (number_of_days % 7)
        if new_day >= 7:
            new_day -= 7
        print(new_day)
        new_time.append(f', {days_of_week[new_day].capitalize()}')
    #if added time rolls over to the next day or so, add to return string
    if number_of_days == 1:
        new_time.append(' (next day)')
    elif number_of_days > 1:
        new_time.append(f' ({number_of_days} days later)')
    return ''.join(new_time)

print(add_time('11:59 AM', '0:01'))