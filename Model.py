'''
Model handles all Task manipulation
'''
import json
from tabnanny import check
from Task import Task
'''
@return Task
'''


def newTask():
    # Prompt the user to ask for details about the task
    name = input('What would you like to call your new task?\n')
    taskType = input(
        'Is this task Transient(1), Recurring(2), or an Anti-Task(3)?\n')
    startTime = input(
        'What time does this task begin? format(hours:minutes 24hr)\n')
    duration = input(
        'How long will this task take? format(days:hours:minutes)\n')
    # If its a recurring task format the question a little differently
    if (taskType == "2"):
        date = input('What day does this task start on? format(mm/dd/yyyy)\n')
    else:
        date = input('What day does this task occur on? format(mm/dd/yyyy)\n')

    # If its a recurring task need a date for when it stops recurring
    if (taskType == "2"):

        # ASSUMING THAT THE TASK DOES NOT GO INTO ANOTHER DAY
        # NEED TO CHECK IF MINUTES EXCEED 60, HOURS EXCEED 24, OR DAYS EXCEED DAYS OF THE MONTH

        """
        startTimes = startTime.split(":")
        startMinutes = int(startTimes[0])*60 + int(startTimes[1])
        durationTimes = duration.split(":")
        durationMinutes = int(durationTimes[0])*60*60 + int(durationTimes[1])*60 + int(durationTimes[2])
        #Check if the task will end on a different day or not
        if(durationMinutes + startMinutes < 24*60):
                endDate = date
        else:
                dateSplit = date.split("/")
                endDate = "/".join([dateSplit[0], str( int(dateSplit[1]) +
                        int((durationMinutes + startMinutes)/ (24*60)) ), dateSplit[2]])
        print("endDate:" + endDate)
        """
        endDate = date
        freq = input(
            'How often does this task recur? (daily, weekly, monthly)\n')
    # Otherwise just set it as -1
    else:
        endDate = -1
        freq = "once"

    # Plug in the details and return the created task
    return Task(name, taskType, startTime, duration, date, endDate, freq)


'''
@param task, Task to add to schedule
@param schedule, Schedule to add task too
@return schedule, unchanged if not valid
'''
# Used to add a created task to a schedule, ensuring no overlap and sorting


def addTask(task, schedule):
    if checkNoOverlap(task, schedule):
        schedule.append(task)
        schedule = sort(schedule)
        return schedule
    return schedule


def sort(schedule):
    return schedule


'''
@param oldTask, Task obj to be deleted
@param schedule, schedule to remove task from
@return schedule
'''


def deleteTask(oldTask, schedule):
    for task in schedule:
        if task == oldTask:
            schedule.remove(oldTask)
            break
    return schedule


'''
@param oldTask, Task obj to be edited
@param schedule, schedule to find task to edit in
@return schedule
'''


def editTask(badTask, schedule):
    # Prompt the user for task details to be modified
    # Name
    prompt = input('would you like to change the task name? (y/n)\n')
    if(prompt == "y"):
        name = input('What would you like to call your task?\n')
    else:
        name = badTask.getName()
    # Task Type
    prompt = input('would you like to change the task type? (y/n)\n')
    if(prompt == "y"):
        taskType = input(
            'Is this task Transient(1), Recurring(2), or an Anti-Task(3)?\n')
    else:
        taskType = badTask.getTaskType()
    # Start Time
    prompt = input('would you like to change the task start time? (y/n)\n')
    if(prompt == "y"):
        startTime = input(
            'What time does this task begin? format(hours:minutes 24hr)\n')
    else:
        startTime = badTask.getStartTime()
    # Duration
    prompt = input('would you like to change the task duration? (y/n)\n')
    if(prompt == "y"):
        duration = input(
            'How long will this task take? format(days:hours:minutes)\n')
    else:
        duration = badTask.getDuration()
    # Check if the task is recurring
    if (taskType == "2"):
        # Date
        prompt = input('would you like to change the task start date? (y/n)\n')
        if(prompt == "y"):
            date = input(
                'What day does this task start on? format(mm/dd/yyyy)\n')
        else:
            date = badTask.getDate()
        # End Date
            # ASSUMING TAKS ENDS ON SAME DATE IT STARTS, NEED TO CHANGE
            endDate = date
        """prompt = input('would you like to change the task end date? (y/n)\n')
                if(prompt == "y"):
                        date = input('What day does this task end on? format(mm/dd/yyyy)\n')
                else:
                        date = badTask.getDate()"""
        # Frequency
        if(badTask.type == "2"):
            prompt = input(
                'would you like to change the task frequency? (y/n)\n')
            if(prompt == "y"):
                freq = input(
                    'How often does this task recur? (daily, weekly, monthly)\n')
            else:
                freq = badTask.getFreq()
        else:
            freq = input(
                'How often does this task recur? (daily, weekly, monthly)\n')

    else:
        # Make sure that endDate is -1 and freq is "once"
        endDate = -1
        freq = "once"
    # Create a new task using any data the user wants to keep
    # from the old task and any new data they entered
    newTask = Task(name, taskType, startTime, duration, date, endDate, freq)
    deleteTask(badTask, schedule)
    schedule = addTask(newTask, schedule)


'''
@return Task
'''


def findTask(schedule):
    # List of tasks with matching names
    nameMatch = []
    # Request the user for the name of the task
    name = input("What is the name of the task?\n")
    # Loop through the entire schedule, looking for tasks with same name
    for task in schedule:
        if(task.getName() == name):
            nameMatch.append(task)
    if(len(nameMatch) == 0):
        print("No task found with that name.")
        return -1
    elif(len(nameMatch) == 1):
        print("Task found.")
        return task
    else:
        # List of tasks with matching names and dates
        dateMatch = []
        # If there are multiple tasks with the same name, ask them for a date
        date = input("What date does the task start on?\n")
        for task in nameMatch:
            if(task.getDate() == date):
                dateMatch.append(task)
        if(len(dateMatch) == 0):
            print("No task found with that name and date.")
            return -1
        elif(len(dateMatch) == 1):
            print("Task found.")
            print(task)
            return task
        else:
            # List of tasks with matching names and dates
            timeMatch = []
            # If there are multiple tasks with the same date ask them for a time
            time = input("What time does the task start?\n")
            for task in dateMatch:
                #######

                # Might want to accept any time in the
                # Tasks entire runtime rather than exactly
                # when they start

                # So a task that starts at 10 and ends at 11
                # would be found if the time entered was 10:30

                #######
                if(task.getStartTime() == time):
                    timeMatch.append(task)
            if(len(timeMatch) == 0):
                print("No task found with that name and date.")
                return -1
            elif(len(timeMatch) == 1):
                print("Task found.")
                print(task)
                return task


'''
@param task, task to add to schedule
@param schedule, schedule to add task too
@return overlapped, True if no overlap False if there is overlap
@throws Exception
'''


def checkNoOverlap(task, schedule):
    # Check if there are tasks with a matching date as new task

    # If there is another task at that date, check if there are tasks
    # In the same time frame
    for t in schedule:
        if(Task.getDate(t) == Task.getDate(task) and Task.getStartTime(t) == Task.getStartTime(task)):
            return False
    return True


'''
@param task, task to find name in schedule
@param schedule, list of tasks
@return unique, True if unique name False if not unique name
'''


def checkUniqueName(task, schedule):
    for t in schedule:
        if(Task.getName(t) == Task.getName(task)):
            return False
    return True


'''
@param task, task to find type 
@return unique, True if valid type  False if not valid type
'''


def checkType(task):
    taskTypes = {
        "Recurring": ["Class", "Study", "Sleep", "Exercise", "Work", "Meal"],
        "Transient": ["Visit", "Shopping", "Appointment"],
        "Anti-Task": ["Cancellation"]
    }

    for type in taskTypes["Recurring"]:
        if(Task.getType(task) == type):
            return True

    for type in taskTypes["Transient"]:
        if(Task.getType(task) == type):
            return True

    for type in taskTypes["Anti-Task"]:
        if(Task.getType(task) == type):
            return True

    return False


'''
@param taskDate, date in format (mm/dd/yyyy)
@return valid, True if mm has respective dd False if not
'''


def checkDate(taskDate):
    cal = {
        "01": "31",
        "02": "28",
        "03": "31",
        "04": "30",
        "05": "31",
        "06": "30",
        "07": "31",
        "08": "31",
        "09": "30",
        "10": "31",
        "11": "30",
        "12": "31"
    }
    dateSplit = taskDate.split("/")  # (mm/dd/yyyy)
    if(cal[dateSplit[0]] == dateSplit[1]):
        return True

    return False


'''
@param f, task frequency
@return valid, True if     False if not
'''


def checkFreq(f):
    freq = {
        "once": "1",
        "daily": "2",
        "weekly": "2"
    }
    if(f in freq):
        return True

    return False


'''
@param fileName, file name of json file
@return schedule, list of user's tasks
@throws Exception
'''


def readFile(fileName):
    sch = []

    # reads file
    jsonfile = open(fileName, 'r')
    jsondata = jsonfile.read()
    # print data
    taskObj = json.loads(jsondata)  # changes data from string into dictionary
    for i in range(len(taskObj)):
        name = taskObj[i].get('Name')
        type = taskObj[i].get('Type')
        startTime = taskObj[i].get('StartTime')
        duration = taskObj[i].get('Duration')
        date = taskObj[i].get('Date')
        endDate = taskObj[i].get('EndDate')
        frequency = taskObj[i].get('Frequency')

        t = Task(name, type, startTime, duration, date,
                 endDate, frequency)  # make new task
        # check for conflicting time
        if(not checkNoOverlap(t, sch)):
            print("ERROR: Overlap in schedule")
            return
        # check for unique task name
        if(not checkUniqueName(t, sch)):
            print("ERROR: No unique task names")
            return
        # check for valid type
        if(not checkType(t)):
            print('ERROR: Invalid type for ', Task.getName(t))
            return
        # check for valid date
        if(not checkDate(date)):
            print('ERROR: Invalid date for ', Task.getName(t))
            return
        # check for valid end date
        if(endDate != -1):
            if(not checkDate(endDate)):
                print('ERROR: Invalid end date for ', Task.getName(t))
                return
        # check for valid frequency
        if(not checkFreq(frequency)):
            print('ERROR: Invalid frequency for ', Task.getName(
                t), ' Type: ', type, ' Freq: ', frequency)
            return
        sch.append(t)  # add to schedule

    jsonfile.close()
    return sch


'''
@param fileName, file name of json file
@param schedule, list of user's tasks
@return void
@throws Exception
'''


def writeFile(fileName, schedule):
    outjson = open(fileName, 'w')

    outjson.write('[\n')
    # If the schedule isnt empty, save all the tasks
    if schedule:
        for task in schedule:
            outjson.write('\t{\n')
            outjson.write("\t\t\"Name\": \"" + task.getName() + "\",\n")
            outjson.write("\t\t\"Type\": \"" + task.getType() + "\",\n")
            outjson.write("\t\t\"Date\": \"" + str(task.getDate()) + "\",\n")
            outjson.write("\t\t\"StartTime\": \"" +
                          str(task.getStartTime()) + "\",\n")
            outjson.write("\t\t\"Duration\": \"" +
                          str(task.getDuration()) + "\",\n")
            outjson.write("\t\t\"EndDate\": \"" +
                          str(task.getEndDate()) + "\",\n")
            outjson.write("\t\t\"Frequency\": \"" +
                          str(task.getFrequency()) + "\"")
            outjson.write('\n\t}')
            # Dont add trailing comma to last item
            if task != schedule[-1]:
                outjson.write(',')
            outjson.write('\n')

    outjson.write('\n]')

    outjson.close()
