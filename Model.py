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
    print('Please enter the task type')
    printTypes()
    type = input()
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
    while startTime > 24.0 or startTime < 0.0 or (((startTime % 1)*10) != 0 and ((startTime % 1)*10) != 2.5 and ((startTime % 1)*10) != 5.0 and ((startTime % 1)*10) != 7.5):
        startTime = float(input(
            'Please enter a valid start time. It must be in 15 minute intervals. (Ex: 1:30 PM = 13.5)\n'))
    duration = float(input(
        'How long will this task take? format(Ex: 2 Hours and 15 Minutes = 2.25)\n'))
    while (((duration % 1)*10) != 0 and ((duration % 1)*10) != 2.5 and ((duration % 1)*10) != 5.0 and ((duration % 1)*10) != 7.5):
        duration = float(input(
            'Please enter a valid duration. It must be in 15 minute intervals. (Ex: 2 Hours and 15 Minutes = 2.25)\n'))

    # If its a recurring task format the question a little differently
    if (taskType == 2):
        startDate = int(input(
            'What day does this task start on? (yyyymmdd)(Ex: May 4, 2022 = 20220604)\n'))
    else:
        startDate = int(input(
            'What day does this task occur on? (yyyymmdd)(Ex: May 4, 2022 = 20220604)\n'))

    # If its a recurring task need a date for when it stops recurring
    if (taskType == 2):
        endDate = int(
            input('What day does this task end? (yyyymmdd)(Ex: May 4, 2022 = 20220604)\n'))
        while endDate < startDate:
            endDate = int(input(
                'The end date must be after the start date. (yyyymmdd)(Ex: May 4, 2022 = 20220604)\n'))
        freq = int(
            input('How often does this task recur? Daily(1) or Weekly(7)\n'))
        while freq != 1 and freq != 7:
            freq = int(input('Please enter 1 for Daily or 7 for Weekly\n'))

    # Otherwise calculate the end Date to make sure it doesnt go past midnight into the next day
    else:
        durationDays = int((duration + startTime)/24)
        remainder = (duration + startTime)%24
        if(durationDays) > 0:
            #Calc end date
            endDate = startDate + durationDays
            #Make sure end date is valid
            if(not checkDate(endDate)):
                endDate = (endDate + 100 - (int(endDate) % 100) + 1)
        #The duration doesnt carry the task to the next day so end date and start date a re the same
        else:
            endDate = startDate
        freq = 0

    # Plug in the details and return the created task
    return Task(name, type, taskType, startTime, duration, startDate, endDate, freq)


'''
@param task, Task to add to schedule
@param schedule, Schedule to add task too
@return schedule, unchanged if not valid
'''

# Used to add a created task to a schedule, ensuring no overlap and sorting

def addTask(task, schedule):
    if checkNoOverlap(task, schedule):
        print("Valid Task")
        schedule.append(task)
        print("Wow")
        schedule = sort(schedule)
        print("Done")
        return schedule
    else:
        print('Invalid Task')
    return schedule

# Sort schedule in ascending order based on date / start time if same date

def sort(schedule):

    # Insertion sort
    for i in range(1, len(schedule)):

        # temporary value to save task at current index i
        temp = schedule[i]
        j = i - 1

        # count down to beginning of schedule from index j = (i - 1)
        # only swap if task start date is less than current
        while (j >= 0 & temp.getStartDate() <= schedule[j].getStartDate()):

            # if two entries have same start date, check start time instead
            if(schedule[j + 1].getStartDate() == schedule[j].getStartDate()):

                # if start times are in order, skip swap at end of loop
                if(schedule[j + 1].getStartTime() >= schedule[j].getStartTime()):
                    continue
            schedule[j + 1] = schedule[j]
            j -= 1
        schedule[j + 1] = temp
    return schedule


'''
@param oldTask, Task obj to be deleted
@param schedule, schedule to remove task from
@return schedule
'''


def deleteTask(oldTask, schedule):
    if oldTask.getTaskType() == 3:
        oldEndDay = oldTask.getStartDate()
        oldEndTime = oldTask.getStartTime() + oldTask.getDuration()
        if oldEndTime > 24:
            oldEndTime -= 24
            oldEndDay += 1
            if not (checkDate(oldEndDay)):
                oldEndDay = (oldEndDay + 100 - (int(oldEndDay) % 100))
        for task in schedule:
            if task.getTaskType() == 1:
                endDay = task.getStartDate()
                endTime = task.getStartTime() + task.getDuration()
                if endTime > 24:
                    endDay += 1
                    if not(checkDate(endDay)):
                        endDay = (endDay+100-(int(endDay)%100))
                if task.getStartDate() == oldTask.getStartDate() or endDay == oldTask.getStartDate():
                    if (oldTask.getStartTime() >= task.getStartTime() and endTime >= oldTask.getStartTime() or
                        (oldEndTime >= task.getStartTime() and endTime >= oldEndTime)):
                        print('Remove denied to prevent overlap due to transient task: ' + task.getName())
                        return schedule
    elif oldTask.getTaskType() == 2:
        wholeSchedule = recSchedule2(schedule)
        deleteArray = []
        for task in schedule:
            if task.getTaskType() == 3:
                for innertask in wholeSchedule:
                    if innertask.getName() == oldTask.getName():
                        if innertask.getStartDate() == task.getStartDate():
                            if int((innertask.getStartTime()*100)) == int((task.getStartTime()*100)):
                                if int((innertask.getDuration()*100)) == int((task.getDuration()*100)):
                                    deleteArray.append(task)
                                    break
        for item in deleteArray:
            schedule.remove(item)
    schedule.remove(oldTask)
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
        print('Please enter the task type')
        printTypes()
        type = input()
        while taskType == 0:
            if (type == "Class" or type == "Study" or type == "Sleep"
                    or type == "Exercise" or type == "Work" or type == "Meal"):
                taskType = 2
            elif type == "Visit" or type == "Shopping" or type == "Appointment":
                taskType = 1
            elif type == "Cancellation":
                taskType = 3
            else:
                print('Please enter a valid type.\n')
                printTypes()
                type = input()
        badTask.setType(type)
        badTask.setTaskType(taskType)

    # Start Time
    prompt = input('Would you like to change the task start time? (y/n)\n')
    if(prompt == "y"):
        startTime = float(input(
            'What time does this task begin? (Ex: 1:30 PM = 13.5)\n'))
        while startTime > 24 or startTime < 0 or (
                ((startTime % 1) * 10) != 0 and ((startTime % 1) * 10) != 2.5 and ((startTime % 1) * 10) != 5.0 and (
                (startTime % 1) * 10) != 7.5):
            startTime = float(
                input('Please enter a valid start time. It must be in 15 minute intervals. (Ex: 1:30 PM = 13.5)\n'))
        badTask.setStartTime(startTime)

    # Duration
    prompt = input('Would you like to change the task duration? (y/n)\n')
    if(prompt == "y"):
        duration = float(input(
            'How long will this task take? format(Ex: 2 Hours and 15 Minutes = 2.25)\n'))
        while (((duration % 1) * 10) != 0 and ((duration % 1) * 10) != 2.5 and ((duration % 1) * 10) != 5.0 and (
                (duration % 1) * 10) != 7.5):
            duration = float(input(
                'Please enter a valid duration. It must be in 15 minute intervals. (Ex: 2 Hours and 15 Minutes = 2.25)\n'))
        badTask.setDuration(duration)

    # Start Date
    prompt = input('Would you like to change the task start date? (y/n)\n')
    if (prompt == "y"):
        startDate = int(input(
            'What day does this task start on? (yyyymmdd)(Ex: May 4, 2022 = 20220604)\n'))
        badTask.setStartDate(startDate)

    # Check if the task is recurring
    if (taskType == 2):

        # End Date
        prompt = input('Would you like to change the task end date? (y/n)\n')
        if (prompt == "y"):
            endDate = int(
                input('What day does this task end? (yyyymmdd)(Ex: May 4, 2022 = 20220604)\n'))
            while endDate < startDate:
                endDate = int(input(
                    'The end date must be after the start date. (yyyymmdd)(Ex: May 4, 2022 = 20220604)\n'))
            badTask.setEndDate(endDate)

        # Frequency
        prompt = input('Would you like to change the frequency (y/n)\n')
        if (prompt == "y"):
            freq = int(
                input('How often does this task recur? Daily(1) or Weekly(7)\n'))
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
        return nameMatch[0]


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
    #     if(Task.getStartDate(t) == Task.getStartDate(task) and Task.getStartTime(t) == Task.getStartTime(task)):
    #         return False
    start = task.getStartDate()
    time = int(task.getStartTime() *100)
    dura = int(task.getDuration()*100)
    end = time + dura
    wholeschedule = recSchedule2(schedule)
    if task.getTaskType() == 1:
        removeTask = []
        for t1 in wholeschedule:
            if t1.getTaskType() == 3:
                removeTask.append(t1)
                for t2 in wholeschedule:
                    if t2.getTaskType() == 2 and t1.getStartDate() == t2.getStartDate():
                        if (int(t2.getStartTime() * 100) == int(t1.getStartTime() * 100) and
                                int(t2.getDuration() * 100) == int(t1.getDuration() * 100)):
                            removeTask.append(t2)
        for item in removeTask:
            wholeschedule.remove(item)
        for t in wholeschedule:
            if t.getStartDate() == start:
                newstart = int(t.getStartTime()*100)
                newend = int(t.getStartTime()*100) + int(t.getDuration()*100)
                if (newstart >= time and end >= newstart) or (newend >= time and end >= newend):
                    return False
                else:
                    continue
        return True
    elif task.getTaskType() == 2:
        for t in wholeschedule:
            if t.getName() != task.getName() and t.getStartDate() == start:
                newstart = int(t.getStartTime()*100)
                newend = int(t.getStartTime()*100) + int(t.getDuration()*100)
                if (time >= newstart and newend >= time) or (end >= newstart and newend >= end):
                    return False
                else:
                    continue
        return True
    elif task.getTaskType() == 3:
        for t in wholeschedule:
            # Check for recurring task on the same day
            if start == t.getStartDate() and t.getTaskType() == 2:
                if time == int(t.getStartTime()*100) and dura == int(t.getDuration()*100):
                    return True
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
@return void
'''

def printTypes():
    taskTypes = {
        "Recurring": ["Class", "Study", "Sleep", "Exercise", "Work", "Meal"],
        "Transient": ["Visit", "Shopping", "Appointment"],
        "Anti-Task": ["Cancellation"]
    }

    print("Available task types:")

    # print("Recurring")
    for type in taskTypes["Recurring"]:
        print(type)

    # print("Transient")
    for type in taskTypes["Transient"]:
        print(type)

    # print("Anti-Task")
    for type in taskTypes["Anti-Task"]:
        print(type)

'''
@param taskDate, date in format (mm/dd/yyyy)
@return valid, True if mm has respective dd False if not
'''

def checkDate(taskDate):
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
    month = int((int(taskDate) % 10000) / 100)
    day = (int(taskDate) % 100)
    if(month > 0 and month < 13 and day > 0 and day <= cal[month]):
        return True
    return False

def checkTime(time):
    if (((time % 1)*10) != 0 and ((time % 1)*10) != 2.5 and ((time % 1)*10) != 5.0 and ((time % 1)*10) != 7.5):
        return False
    return True

'''
@param fileName, file name of json file
@return schedule, list of user's tasks
@throws Exception
'''

def readFile(fileName,sch):

    # reads file
    jsonfile = open(fileName, 'r')
    jsondata = jsonfile.read()

    # print data
    taskObj = json.loads(jsondata)  # changes data from string into dictionary
    for i in range(len(taskObj)):
        name = taskObj[i].get('Name')
        type = taskObj[i].get('Type')

        # taskType = 0
        if (type == "Class" or type == "Study" or type == "Sleep"
                or type == "Exercise" or type == "Work" or type == "Meal"):
            taskType = 2
        elif type == "Visit" or type == "Shopping" or type == "Appointment":
            taskType = 1
        elif type == "Cancellation":
            taskType = 3
        if taskType == 2:
            startTime = float(taskObj[i].get('StartTime'))
            duration = float(taskObj[i].get('Duration'))
            startDate = int(taskObj[i].get('StartDate'))
            endDate = int(taskObj[i].get('EndDate'))
            frequency = int(taskObj[i].get('Frequency'))
        elif taskType == 1 or taskType == 3:
            startTime = float(taskObj[i].get('StartTime'))
            duration = float(taskObj[i].get('Duration'))
            startDate = int(taskObj[i].get('Date'))
            endDate = -1
            frequency = 0
        t = Task(name, type, taskType, startTime, duration, startDate,
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
            printTypes()
            return

        # check for valid start date
        if(not checkDate(startDate)):
            print('ERROR: Invalid date for ', Task.getName(t))
            return

        # check for valid start time
        if (not checkTime(startTime)) or startTime < 0 or startTime >= 24:
            print('ERROR: Invalid start time for ', Task.getName(t))
            return

        # check for valid duration
        if (not checkTime(duration)):
            print('ERROR: Invalid duration for ', Task.getName(t))
            return

        # check for valid end date
        if(endDate != -1):
            if(not checkDate(endDate)):
                print('ERROR: Invalid end date for ', Task.getName(t))
                return


        # check for valid frequency
        if frequency != 0:
            if(frequency != 1 and frequency != 7):
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
            if task.getTaskType() == 2:
                outjson.write('\t{\n')
                outjson.write("\t\t\"Name\": \"" + task.getName() + "\",\n")
                outjson.write("\t\t\"Type\": \"" + task.getType() + "\",\n")
                outjson.write("\t\t\"StartDate\": \"" +
                              str(task.getStartDate()) + "\",\n")
                outjson.write("\t\t\"StartTime\": \"" +
                              str(task.getStartTime()) + "\",\n")
                outjson.write("\t\t\"Duration\": \"" +
                              str(task.getDuration()) + "\",\n")
                outjson.write("\t\t\"EndDate\": \"" +
                              str(task.getEndDate()) + "\",\n")
                outjson.write("\t\t\"Frequency\": \"" +
                              str(task.getFrequency()) + "\"")
                outjson.write('\n\t}')
            elif task.getTaskType() == 1 or task.getTaskType() == 3:
                outjson.write('\t{\n')
                outjson.write("\t\t\"Name\": \"" + task.getName() + "\",\n")
                outjson.write("\t\t\"Type\": \"" + task.getType() + "\",\n")
                outjson.write("\t\t\"Date\": \"" +
                              str(task.getStartDate()) + "\",\n")
                outjson.write("\t\t\"StartTime\": \"" +
                              str(task.getStartTime()) + "\",\n")
                outjson.write("\t\t\"Duration\": \"" +
                              str(task.getDuration()) + "\",\n")
                outjson.write('\n\t}')
            # Dont add trailing comma to last item
            if task != schedule[-1]:
                outjson.write(',')
            outjson.write('\n')

    outjson.write(']')

    outjson.close()

'''
@param fileName, file name of json file
@param schedule, list of user's tasks
@param day, start day to write tasks
@param opt, day is 1, week, is 2, month is 3
@return void
@throws Exception
'''

def altWriteFile(fileName, schedule, date, opt):
    '''
    - write all of the tasks for that time period, in sorted order
    - anti-task, both it and the recurring task instance it cancels will not be included in the list
    - recurring task will not be displayed as a single entry.  Rather, each instance
    '''

    if(not checkDate(date)):
        print("Invalid Input Date:", str(date))
        print("No tasks written to", fileName)
        return

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

    count = 0
    altSchedule = []

    # date format yyyymmdd
    #calculate the end day based on input
    if opt == 1:  # write day
        endDay = date

    if opt == 2:  # write week
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

    if opt == 3:  # write month
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

    rec = recSchedule(schedule)
    for task in rec:
        d = Task.getStartDate(task)
        if d >= date and d <= endDay:
            count = count + 1
            altSchedule.append(task)

    outjson = open(fileName, 'w')

    # If the schedule isnt empty, save all the tasks
    if altSchedule:
        outjson.write('[\n')
        for task in altSchedule:
            outjson.write('\t{\n')
            outjson.write("\t\t\"Name\": \"" + task.getName() + "\",\n")
            outjson.write("\t\t\"Type\": \"" + task.getType() + "\",\n")
            outjson.write("\t\t\"StartDate\": \"" +
                          str(task.getStartDate()) + "\",\n")
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
            if task != altSchedule[-1]:
                outjson.write(',')
            outjson.write('\n')

        outjson.write(']')

    outjson.close()

    if opt == 1:
        print(count, 'task(s) on', date, 'added to', fileName)
    else:
        print(count, 'task(s) from', date, 'through',
              endDay, 'added to', fileName)

'''
@param schedule, list of user's tasks
@return rec, recurring tasks appear as transient tasks repeating
'''

def recSchedule(schedule):
    rec = []

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

    for task in schedule:

        # print('task #', Task.getTaskType(task))
        if Task.getTaskType(task) == 2:
            freq = Task.getFrequency(task)  # either 1 or 7
            currDate = Task.getStartDate(task)
            # print(type(currDate))
            endDate = Task.getEndDate(task)

            name = Task.getName(task) 
            typ = Task.getType(task)
            startTime = Task.getStartTime(task)
            dur = Task.getDuration(task)

            #change recursive task to transient
            taskType = 1
            endDay = -1
            f = 0

            while currDate <= endDate:
                tempTask = Task(name, typ, taskType,startTime,dur,currDate,endDay, f)
                rec.append(tempTask)

                currDate = currDate + freq

                # check if overflow of week/month/year
                day = (int(currDate) % 100)
                year = int((int(currDate) % 100000000) / 10000)
                month = int((int(currDate) % 10000) / 100)

                # if the day is past month's last day, increment month, set day as the difference
                if day > cal[month]:
                    diff = day - cal[month]

                    if month != 12:
                        currDate = (year*10000) + (month+1)*100 + diff
                    # if december change to january
                    else:
                        currDate = (year+1)*10000 + 100 + diff

        else:
            rec.append(task)

    return rec

def recSchedule2(schedule):
    rec = []

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

    for task in schedule:

        # print('task #', Task.getTaskType(task))
        if Task.getTaskType(task) == 2:
            freq = Task.getFrequency(task)  # either 1 or 7
            currDate = Task.getStartDate(task)
            # print(type(currDate))
            endDate = Task.getEndDate(task)

            name = Task.getName(task)
            typ = Task.getType(task)
            startTime = Task.getStartTime(task)
            dur = Task.getDuration(task)

            #change recursive task to transient
            taskType = 2
            endDay = -1
            f = 0

            while currDate <= endDate:
                tempTask = Task(name, typ, taskType,startTime,dur,currDate,endDay, f)
                rec.append(tempTask)

                currDate = currDate + freq

                # check if overflow of week/month/year
                day = (int(currDate) % 100)
                year = int((int(currDate) % 100000000) / 10000)
                month = int((int(currDate) % 10000) / 100)

                # if the day is past month's last day, increment month, set day as the difference
                if day > cal[month]:
                    diff = day - cal[month]

                    if month != 12:
                        currDate = (year*10000) + (month+1)*100 + diff
                    # if december change to january
                    else:
                        currDate = (year+1)*10000 + 100 + diff

        else:
            rec.append(task)

    return rec