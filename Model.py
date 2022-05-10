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
    type = input('Please enter the task type (Ex: Sleep)\n')
    taskType = 0
    while taskType == 0:
        if (type == "Class" or type == "Study" or type == "Sleep"
        or type == "Exercise" or type == "Work" or type == "Meal"):
            taskType = 2
        elif type == "Visit" or type == "Shopping" or type == "Appointment":
            taskType = 1
        elif type == "Cancellation":
            taskType = 3
        else:
            print("Please enter a valid type.\nAvailable task types:")
            printTypes()
            type = input()
    startTime = float(input(
        'What time does this task begin? (Ex: 1:30 PM = 13.5)\n'))
    while startTime > 24 or startTime<0:
        startTime = float(input('Please enter a valid start time. (Ex: 1:30 PM = 13.5)\n'))
    duration = float(input('How long will this task take? format(Ex: 2 Hours and 15 Minutes = 2.25)\n'))
    # If its a recurring task format the question a little differently
    if (taskType == 2):
        date = int(input('What day does this task start on? (yyyymmdd)(Ex: May 14, 2022 = 20220614)\n'))
    else:
        date = int(input('What day does this task occur on? (yyyymmdd)(Ex: May 14, 2022 = 20220614)\n'))

    # If its a recurring task need a date for when it stops recurring
    if (taskType == 2):
        endDate = int(input('What day does this task end? (yyyymmdd)(Ex: May 14, 2022 = 20220614)\n'))
        while endDate < date:
            endDate = int(input('The end date must be after the start date. (yyyymmdd)(Ex: May 14, 2022 = 20220614)\n'))
        freq = int(input('How often does this task recur? Daily(1) or Weekly(7)\n'))
        while freq != 1 and freq != 7:
            freq = int(input('Please enter 1 for Daily or 7 for Weekly\n'))
    # Otherwise just set it as -1
    else:
        endDate = -1
        freq = 0

    # Plug in the details and return the created task
    return Task(name, type, taskType, startTime, duration, date, endDate, freq)


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


def editTask(badTask):
    # Prompt the user for task details to be modified
    # Name
    prompt = input('Would you like to change the task name? (y/n)\n')
    if(prompt == "y"):
        name = input('What would you like to call your task?\n')
        badTask.setName(name)
    # Type
    prompt = input('Would you like to change the task type? (y/n)\n')
    taskType = 0
    if(prompt == "y"):
        type = input('Please enter the task type (Ex: Sleep)\n')
        while taskType == 0:
            if (type == "Class" or type == "Study" or type == "Sleep"
                    or type == "Exercise" or type == "Work" or type == "Meal"):
                taskType = 2
            elif type == "Visit" or type == "Shopping" or type == "Appointment":
                taskType = 1
            elif type == "Cancellation":
                taskType = 3
            else:
                type = input('Please enter a valid type. (Ex: Class or Visit)\n')
        badTask.setType(type)
        badTask.setTaskType(taskType)
    # Start Time
    prompt = input('Would you like to change the task start time? (y/n)\n')
    if(prompt == "y"):
        startTime = float(input(
            'What time does this task begin? (Ex: 1:30 PM = 13.5)\n'))
        while startTime > 24 or startTime < 0:
            startTime = float(input('Please enter a valid start time. (Ex: 1:30 PM = 13.5)\n'))
        badTask.setStartTime(startTime)
    # Duration
    prompt = input('Would you like to change the task duration? (y/n)\n')
    if(prompt == "y"):
        duration = float(input('How long will this task take? format(Ex: 2 Hours and 15 Minutes = 2.25)\n'))
        badTask.setDuration(duration)
    # Check if the task is recurring
    if (taskType == 2):
        # Date
        prompt = input('Would you like to change the task start date? (y/n)\n')
        if(prompt == "y"):
            date = int(input('What day does this task start on? (yyyymmdd)(Ex: May 14, 2022 = 20220614)\n'))
            badTask.setDate(date)
        # End Date
        prompt = input('Would you like to change the task end date? (y/n)\n')
        if (prompt == "y"):
            endDate = int(input('What day does this task end? (yyyymmdd)(Ex: May 14, 2022 = 20220614)\n'))
            while endDate < date:
                endDate = int(input('The end date must be after the start date. (yyyymmdd)(Ex: May 14, 2022 = 20220614)\n'))
            badTask.setEndDate(endDate)
        # Frequency
        prompt = input('Would you like to change the frequency (y/n)\n')
        if (prompt == "y"):
            freq = int(input('How often does this task recur? Daily(1) or Weekly(7)\n'))
            while freq != 1 and freq != 7:
                freq = int(input('Please enter 1 for Daily or 7 for Weekly\n'))
            badTask.setFrequency(freq)


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
    # for t in schedule:
    #     if(Task.getDate(t) == Task.getDate(task) and Task.getStartTime(t) == Task.getStartTime(task)):
    #         return False
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
@return void
'''

def printTypes():
    taskTypes = {
        "Recurring": ["Class", "Study", "Sleep", "Exercise", "Work", "Meal"],
        "Transient": ["Visit", "Shopping", "Appointment"],
        "Anti-Task": ["Cancellation"]
    }
    #print("Recurring")
    for type in taskTypes["Recurring"]:
        print(type)

    #print("Transient")
    for type in taskTypes["Transient"]:
        print(type)

    #print("Anti-Task")
    for type in taskTypes["Anti-Task"]:
        print(type)
    


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
            print("Available task types:")
            printTypes()
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
