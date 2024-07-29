interval_start_hours, interval_start_minutes = int(input()), int(input())
interval_number = 1

def calculate_and_print_interval():
    global interval_start_hours, interval_start_minutes, interval_number

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

    # Зададим начало следующего интервала
    interval_start_hours = int(interval_stop_hours)
    interval_start_minutes = int(interval_stop_minutes) + 17 # смещение 17 минут
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
    while True:
        print()
        calculate_and_print_interval()
        print()
        
        answer = input('Next (y/n)? ')
        if answer == 'y':
            interval_number += 1
            continue
        elif answer == 'n':
            break