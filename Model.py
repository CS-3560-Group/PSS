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
@param name, string of task name
@return void
'''


def deleteTask(name):
	print('deleteTask')


'''
@param name, string of task name
@return Task
'''


def editTask(name):
	print('editTask')


'''
@param fileName, file name of json file
@return schedule, list of user's tasks
@throws Exception
'''


'''
@return Task
'''
def findTask():
        #Request 
        pass


'''
@param task, task to add to schedule
@param schedule, schedule to add task too
@return overlapped, True if no overlap False if there is overlap
@throws Exception
'''
def checkOverlap(task, schedule):
        pass


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
