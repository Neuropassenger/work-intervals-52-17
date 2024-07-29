interval_start_hours, interval_start_minutes = int(input('Hours: ')), int(input('Minutes: '))

def calculate_and_print_interval(interval_number):
    global interval_start_hours, interval_start_minutes

    interval_stop_hours = interval_start_hours
    interval_stop_minutes = interval_start_minutes + 52

    if interval_stop_minutes > 59:
        interval_stop_hours += 1
        interval_stop_minutes -= 60
    
    if interval_stop_hours == 24:
        interval_stop_hours = 0

    interval_start_hours = maybe_add_zero_symbol(interval_start_hours)
    interval_start_minutes = maybe_add_zero_symbol(interval_start_minutes)
    interval_stop_hours = maybe_add_zero_symbol(interval_stop_hours)
    interval_stop_minutes = maybe_add_zero_symbol(interval_stop_minutes)

    print('[Interval #' + str(interval_number) + '] ' + interval_start_hours + ':' + interval_start_minutes + ' - ' + interval_stop_hours + ':' + interval_stop_minutes)

    # Set the beginning of the next interval
    interval_start_hours = int(interval_stop_hours)
    interval_start_minutes = int(interval_stop_minutes) + 17 # offset of 17 minutes
    if interval_start_minutes > 59:
        interval_start_hours = int(interval_start_hours) + 1
        interval_start_minutes -= 60

    if interval_start_hours == 24:
        interval_start_hours = 0

def maybe_add_zero_symbol(number):
    if int(number) < 10:
        return '0' + str(number)
    else:
        return str(number)

if __name__ == "__main__":
    answer = int(input('How many intervals? '))
    print()
    for i in range(answer):
        calculate_and_print_interval(i + 1)