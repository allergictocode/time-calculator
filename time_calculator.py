def add_time(start, duration, day_name=None):

    # split start into variables
    time, meridiem = start.split()
    hour, min = time.split(':')
    dur_hour, dur_min = duration.split(':')
    hour = int(hour)
    min = int(min)
    dur_hour = int(dur_hour)
    dur_min = int(dur_min)

    # 24-hour format
    if meridiem == "PM":
      hour += 12
 
    # calculate total hour, total min, days, meridiem
    total_min = min + dur_min
    total_hour = hour + dur_hour

    days = 0
    if total_min >= 60:
      h, m = divmod(total_min, 60)
      total_hour += h
      total_min = m
    if total_hour > 11:
      meridiem = "PM"      
      if total_hour == 24:
        total_hour = 12
        days += 1      
      if total_hour > 24:
        day, hr = divmod(total_hour, 24)
        days += day
        if hr == 0:
          total_hour = 12
          meridiem = 'AM'
        elif hr <= 11:
          meridiem = 'AM'
          total_hour = hr      
        else:
          meridiem = "PM"
          if hr == 12:
            total_hour = hr        
          else:
            total_hour = hr - 12
      if total_hour > 12:
        total_hour -= 12
          
    # new minute 24-hour format
    if total_min <= 9:
      new_min = '0' + str(total_min)
    else:
      new_min = str(total_min)

    new_hour = str(total_hour)
    new_meridiem = meridiem  

    # calculate name of day, return new time
    day_dict = {
      'monday': 0,
      'tuesday': 1,
      'wednesday': 2,
      'thursday': 3,
      'friday': 4,
      'saturday': 5,
      'sunday': 6
    }
    if day_name == None:
      if days == 1:
        new_day = '(next day)'
        return f'{new_hour}:{new_min} {new_meridiem} {new_day}'
      elif days > 1:
        new_day = '(' + str(days) + ' days later' + ')'
        return f'{new_hour}:{new_min} {new_meridiem} {new_day}'
      else:
        return f'{new_hour}:{new_min} {new_meridiem}'
    else:
      day_count = (day_dict[day_name.lower()] + days) % 7
      for key, value in day_dict.items():
          if day_count == value:
              day_ans = key
              day_ans = day_ans.capitalize()
              break
      if days == 1:
        new_day = '(next day)'
        return f'{new_hour}:{new_min} {new_meridiem}, {day_ans} {new_day}'
      elif days > 1:
        new_day = '(' + str(days) + ' days later' + ')'
        return f'{new_hour}:{new_min} {new_meridiem}, {day_ans} {new_day}'
      else:
        return f'{new_hour}:{new_min} {new_meridiem}, {day_ans}'
