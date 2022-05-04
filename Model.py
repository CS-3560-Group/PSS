'''
Model handles all Task manipulation
'''
import json
from Task import Task
'''
@return Task
'''
def newTask():
        #Prompt the user to ask for details about the task
        name = input('What would you like to call your new task?\n')
        taskType = input('Is this task Transient(1), Recurring(2), or an Anti-Task(3)?\n')
        startTime = input('What time does this task begin? format(hours:minutes 24hr)\n')
        duration = input('How long will this task take? format(days:hours:minutes)\n')
        #If its a recurring task format the question a little differently
        if (taskType == "2"):
                date = input('What day does this task start on? format(mm/dd/yyyy)\n')
        else:
                date = input('What day does this task occur on? format(mm/dd/yyyy)\n')

        #If its a recurring task need a date for when it stops recurring
        if (taskType == "2"):
                endDate = input()
                freq = input('How often does this task recur? (daily, weekly, monthly)\n')
        #Otherwise just set it as -1
        else:
                endDate = -1
                freq = "once"
                
        #Plug in the details and return the created task
        return Task(name, taskType, startTime, duration, date, endDate, freq)

'''
@param task, Task to add to schedule
@param schedule, Schedule to add task too
@return schedule, unchanged if not valid
'''
#Used to add a created task to a schedule, ensuring no overlap and sorting
def addTask(task, schedule):
        if checkNoOverlap():
                schedule.append(task)
                schedule = sort(schedule)
                return schedule
        return schedule

'''
@param oldTask, Task obj to be deleted
@param schedule, schedule to remove task from
@return void
'''
def deleteTask(oldTask, schedule):
	print('deleteTask')
	for task in schedule:
                if task == oldTask:
                        schedule.remove(oldTask)
                        break
        return schedule


'''
@param name, string of task name
@return Task
'''


def editTask(name):
	print('editTask')
	#Prompt the user for task details to be modified
                        #Name
                        prompt = input('would you like to change the task name? (y/n)')
                        if(prompt == "y"):
                                name = input('What would you like to call your task?\n')
                        else:
                                name = badTask.getName()
                        #Task Type
                        prompt = input('would you like to change the task type? (y/n)')
                        if(prompt == "y"):
                                taskType = input('Is this task Transient(1), Recurring(2), or an Anti-Task(3)?\n')
                        else:
                                taskType = badTask.getTaskType()
                        #Start Time
                        prompt = input('would you like to change the task start time? (y/n)')
                        if(prompt == "y"):
                                startTime = input('What time does this task begin? format(hours:minutes 24hr)\n')
                        else:
                                startTime = badTask.getStartTime()
                        #Duration
                        prompt = input('would you like to change the task duration? (y/n)')
                        if(prompt == "y"):
                                duration = input('How long will this task take? format(days:hours:minutes)\n')
                        else:
                                duration = badTask.getDuration()
                        #Check if the task is recurring
                        if (badTask.taskType == "2"):
                                #Date
                                prompt = input('would you like to change the task start date? (y/n)')
                                if(prompt == "y"):
                                        date = input('What day does this task start on? format(mm/dd/yyyy)\n')
                                else:
                                        date = badTask.getDate()
                                #Frequency
                                prompt = input('would you like to change the task frequency? (y/n)')
                                                                if(prompt == "y"):
                                        freq = input('How often does this task recur? (daily, weekly, monthly)\n')
                                else:
                                        freq = badTask.getFreq()

                        else:
                                #Make sure that endDate is -1 and freq is "once"
                                endDate = -1
                                freq = "once"
                        #Create a new task using any data the user wants to keep
                        #from the old task and any new data they entered
                        newTask = Task(name, taskType, startTime, duration, date, endDate, freq)
                        m.deleteTask(badTask, schedule)
                        schedule = m.addTask(newTask, schedule)


'''
@param fileName, file name of json file
@return schedule, list of user's tasks
@throws Exception
'''


'''
@return Task
'''
def findTask(schedule):
        #List of tasks with matching names
        nameMatch = []
        #Request the user for the name of the task
        name = input()
        #Loop through the entire schedule, looking for tasks with same name
        for task in schedule:
                if(task.getName() == name):
                        nameMatch.append(task)
        if(len(nameMatch) == 0):
                print("No task found with that name.")
                return -1
        elif(len(nameMatch) == 1):
                print("Task found.")
                print(task)
                return task
        else:      
                #List of tasks with matching names and dates
                dateMatch = []          
                #If there are multiple tasks with the same name, ask them for a date
                date = input()
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
                        #List of tasks with matching names and dates
                        timeMatch = []        
                        #If there are multiple tasks with the same date ask them for a time
                        time = input()
                        for task in dateMatch:
                                #######

                                #Might want to accept any time in the
                                #Tasks entire runtime rather than exactly
                                #when they start

                                #So a task that starts at 10 and ends at 11
                                #would be found if the time entered was 10:30

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
        #Check if there are tasks with a matching date as new task

        #If there is another task at that date, check if there are tasks
        #In the same time frame
        return True


def readFile(fileName):
	print('readFile')

	sch = []

	#reads file
	jsonfile = open(fileName,'r')
	jsondata = jsonfile.read()

	#print data
	taskObj = json.loads(jsondata) #changes data from string into dictionary
	for i in range(len(taskObj)):
		name = taskObj[i].get('Name')
		type = taskObj[i].get('Type')
		startTime = taskObj[i].get('StartTime')
		duration = taskObj[i].get('Duration')
		date = taskObj[i].get('Date')
		endDate = taskObj[i].get('EndDate')
		frequency = taskObj[i].get('Frequency')

		t = Task(name, type, startTime, duration, date, endDate,frequency) #make new task
		#add check for conflicting time
		sch.append(t) #add to schedule

	jsonfile.close()
	return sch
		

'''
@param fileName, file name of json file
@param schedule, list of user's tasks
@return void
@throws Exception
'''


def writeFile(fileName, schedule):
	print('writeFile')
	outjson = open(fileName, 'w')
	counter = 0

	outjson.write('[\n')
	
	#output with trailing comma
	while counter < len(schedule)-1:
		# for x in schedule:
			x = schedule[counter]
			outjson.write('\t{\n')
			outjson.write("\t\t\"Name\": \"" + Task.getName(x) + "\",\n")
			outjson.write("\t\t\"Type\": \"" + Task.getType(x) + "\",\n")
			outjson.write("\t\t\"Date\": \"" + str(Task.getDate(x)) + "\",\n")
			outjson.write("\t\t\"StartTime\": \"" + str(Task.getStartTime(x)) + "\",\n")
			outjson.write("\t\t\"Duration\": \"" + str(Task.getDuration(x)) + "\",\n")
			outjson.write("\t\t\"EndDate\": \"" + str(Task.getEndDate(x)) + "\",\n")
			outjson.write("\t\t\"Frequency\": \"" + str(Task.getFrequency(x)) + "\"")

			outjson.write('\n\t},\n') #trailing comma
			counter = counter +1
		
	else:
		x = schedule[counter-1]
		outjson.write('\t{\n')
		outjson.write("\t\t\"Name\": \"" + Task.getName(x) + "\",\n")
		outjson.write("\t\t\"Type\": \"" + Task.getType(x) + "\",\n")
		outjson.write("\t\t\"Date\": \"" + str(Task.getDate(x)) + "\",\n")
		outjson.write("\t\t\"StartTime\": \"" + str(Task.getStartTime(x)) + "\",\n")
		outjson.write("\t\t\"Duration\": \"" + str(Task.getDuration(x)) + "\",\n")
		outjson.write("\t\t\"EndDate\": \"" + str(Task.getEndDate(x)) + "\",\n")
		outjson.write("\t\t\"Frequency\": \"" + str(Task.getFrequency(x)) + "\"")

		outjson.write('\n\t}')  # trailing comma


	outjson.write('\n]')

	outjson.close()
