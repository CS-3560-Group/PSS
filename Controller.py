'''
Controller is responsible for interaction with the user to 
the Viewer and Model
'''

from Task import Task
import Viewer as v
import Model as m


def main():
	print('Welcome to PSS')
	testTask = Task("test", "Transient", 1100, 100, 20220428, 20220429, 1)
	schedule = []
	v.viewTask(schedule, 1)
	v.viewSchedule(schedule)

	m.createTask()
	m.deleteTask("test")
	m.editTask("test")
	m.readFile("schedule.json")
	m.writeFile("schedule.json", schedule)


if __name__ == '__main__':
	main()
