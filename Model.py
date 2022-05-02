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
	taskObj = json.loads(jsondata)
	for i in range(len(taskObj)):
		name = taskObj[i].get('Name')
		type = taskObj[i].get('Type')
		startTime = taskObj[i].get('StartTime')
		duration = taskObj[i].get('Duration')
		startDate = taskObj[i].get('StartDate')
		endDate = taskObj[i].get('EndDate')
		frequency = taskObj[i].get('Frequency')

		t = Task(name, type, startTime, duration, startDate, endDate,frequency)
		sch.append(t)
		
	return sch
		

'''
@param fileName, file name of json file
@param schedule, list of user's tasks
@return void
@throws Exception
'''


def writeFile(fileName, schedule):
	print('writeFile')
