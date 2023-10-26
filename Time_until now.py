from time import *
from datetime import datetime
while True:
    try:
        user_input = input('Enter the goal and a deadline separated by a colon: ')
        input_list = user_input.split(':')
        goal = input_list[0]
        deadline = input_list[1]

        deadline_date = datetime.strptime(deadline, '%d-%m-%Y')
        today_date = datetime.today()
        print(today_date)
        time_till = deadline_date - today_date
        choice = int(input('Enter the output style: \n1. Days \n2. Hours \n3. Minutes\n '))
        if choice == 1:
            print(f'Dear user, the time remaining for your goal: {goal} is {time_till.days} days')
        elif choice == 2:
            print(f'Dear user, the time remaining for your goal: {goal} is {int(time_till.total_seconds()/60/60)} hours')
        elif choice == 3:
            print(f'Dear user, the time remaining for your goal: {goal} is {float(time_till.total_seconds()/60)} minutes')
    except ValueError:
        print('Something went wrong')
















