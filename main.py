interval_1_start_hours, interval_1_start_minutes = int(input()), int(input())

def calculate_and_print_intervals():
    global interval_1_start_hours, interval_1_start_minutes
    interval_1_stop_hours = int(interval_1_start_hours)
    interval_1_stop_minutes = int(interval_1_start_minutes) + 52

    if interval_1_stop_minutes > 59:
        interval_1_stop_hours += 1
        interval_1_stop_minutes -= 60

    if interval_1_stop_hours == 24:
        interval_1_stop_hours = 0

    interval_2_start_hours = interval_1_stop_hours
    interval_2_start_minutes = interval_1_stop_minutes + 17

    if interval_2_start_minutes > 59:
        interval_2_start_hours += 1
        interval_2_start_minutes -= 60

    if interval_2_start_hours == 24:
        interval_2_start_hours = 0

    interval_2_stop_hours = interval_2_start_hours
    interval_2_stop_minutes = interval_2_start_minutes + 52

    if interval_2_stop_minutes > 59:
        interval_2_stop_hours += 1
        interval_2_stop_minutes -= 60

    if interval_2_stop_hours == 24:
        interval_2_stop_hours = 0

    interval_1_start_hours = maybe_add_zero_symbol(interval_1_start_hours)
    interval_1_start_minutes = maybe_add_zero_symbol(interval_1_start_minutes)
    interval_1_stop_hours = maybe_add_zero_symbol(interval_1_stop_hours)
    interval_1_stop_minutes = maybe_add_zero_symbol(interval_1_stop_minutes)

    interval_2_start_hours = maybe_add_zero_symbol(interval_2_start_hours)
    interval_2_start_minutes = maybe_add_zero_symbol(interval_2_start_minutes)
    interval_2_stop_hours = maybe_add_zero_symbol(interval_2_stop_hours)
    interval_2_stop_minutes = maybe_add_zero_symbol(interval_2_stop_minutes)

    print(interval_1_start_hours + ':' + interval_1_start_minutes + ' - ' + interval_1_stop_hours + ':' + interval_1_stop_minutes)
    print(interval_2_start_hours + ':' + interval_2_start_minutes + ' - ' + interval_2_stop_hours + ':' + interval_2_stop_minutes)

    interval_1_start_hours = int(interval_2_stop_hours)
    interval_1_start_minutes = int(interval_2_stop_minutes) + 17

    if interval_1_start_minutes > 59:
        interval_1_start_hours += 1
        interval_1_start_minutes -= 60

def maybe_add_zero_symbol(number):
    if int(number) < 10:
        return '0' + str(number)
    else:
        return str(number)

if __name__ == "__main__":
    while True:
        print()
        calculate_and_print_intervals()
        print()
        
        answer = input('Next (y/n)? ')
        if answer == 'y':
            continue
        elif answer == 'n':
            break