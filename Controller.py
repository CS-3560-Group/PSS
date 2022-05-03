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
	testTask2 = Task("test2", "Recurring", 1111, 111, 20220428, 20220429, 1)
	schedule = []
	schedule.append(testTask)
	schedule.append(testTask2)
	for x in schedule:
		print(x)

	v.viewTask(schedule, 1)
	v.viewSchedule(schedule)

	m.createTask()
	m.deleteTask("test")
	m.editTask("test")
	s = m.readFile("scheduleTester.json")
	for x in s:
		print(x)
	m.writeFile("out.json", schedule)


if __name__ == '__main__':
	main()
