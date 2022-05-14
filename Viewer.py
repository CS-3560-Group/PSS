'''
Viewer displays the user's task for one day, 
one week, one month, 
'''

'''
@param schedule, list of user tasks
@param opt, integer represents view schedule for one day(1),
week(2), or month(3)
@return void
'''




from Task import Task
import Model as m
def viewTask(schedule):
    badTask = m.findTask(schedule)
    if badTask != None:
        print(badTask)


'''
@param schedule, list of user tasks
@return void
'''


def altViewSchedule(schedule, date, opt):
            
    cal = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if schedule:
        r = m.recSchedule(schedule)


        if opt == 4:  # entire schedule
            viewSchedule(r)

        # calculate the end date for month/week/day
        if opt == 3:  # month
            endDay = date + 100

            # check if overflow of month
            day = (int(endDay) % 100)
            year = int((int(date) % 100000000) / 10000)
            month = int((int(endDay) % 10000) / 100)

            # if december change to january
            if month > 12:
                endDay = (year+1)*10000 + 100 + day

            day = (int(endDay) % 100)
            year = int((int(date) % 100000000) / 10000)
            month = int((int(endDay) % 10000) / 100)

            # if days are greater than respective month
            if day > cal[month]:
                endDay = year*10000 + month*100 + cal[month]

        elif opt == 2:  # week
            endDay = date + 7  # check if overflow of week
            # if the day is past month's last day, increment month, set day as the difference

            day = (int(endDay) % 100)
            year = int((int(date) % 100000000) / 10000)
            month = int((int(endDay) % 10000) / 100)

            if day > cal[month]:
                diff = day - cal[month]

                if month != 12:
                        endDay = (year*10000) + (month+1)*100 + diff
                else:
                    endDay = (year+1)*10000 + 100 + diff


        else:  # day
            endDay = date

        for task in r:
            d = Task.getStartDate(task)
            if d >= date and d <= endDay:
                print(task)

    else:
        print("Schedule Empty.")


'''
@param schedule, list of user tasks
@return void
'''


def viewSchedule(schedule):
    if schedule:
               for task in schedule:
                       print(task)
    else:
               print("Schedule Empty.")
