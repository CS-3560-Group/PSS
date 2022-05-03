'''
Model handles all Task manipulation
'''
import json
from Task import Task
'''
@return Task
'''
def createTask():
	print('createTask')


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
	outjson = open('out.json', 'w')
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
