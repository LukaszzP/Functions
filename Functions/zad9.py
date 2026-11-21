def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f'{hours:02d}:{minutes:02d}'
    elif time_format == '12':
        suffix = 'am' if hours < 12 else 'pm'
        h12 = hours % 12
        if h12 == 0:
            h12 = 12
        return f'{h12}:{minutes:02d}{suffix}'

# Testy
print(time_string(15, 38, '24')) # '15:38'
print(time_string(8, 3, '24'))   # '08:03'
print(time_string(0, 5, '24'))   # '00:05'
print(time_string(11, 15, '12')) # '11:15am'
print(time_string(0, 7, '12'))   # '12:07am'
print(time_string(7, 30, '12'))  # '7:30am'
print(time_string(12, 46, '12')) # '12:46pm'
print(time_string(13, 10, '12')) # '1:10pm'
print(time_string(19, 2, '12'))  # '7:02pm'