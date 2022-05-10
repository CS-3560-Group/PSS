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
                return badTask

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
