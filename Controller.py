'''
Controller is responsible for interaction with the user to 
the Viewer and Model
'''

from Task import Task
import Viewer as v
import Model as m
import traceback

def main():
        #Where to save schedule to
        saveFile = "PSS_Schedule.json"
        #Variable to enable or disable debugging
        debug = False
        print('Welcome to PSS')
        print('Checking for existing schedule')
        #Try and load an existing schedule if there is one
        try:
                schedule = m.readFile(saveFile)
                print('Schedule found:')
                v.viewSchedule(schedule)
        except Exception :
                traceback.print_exc()
                print('No existing schedule found, creating a new one.')
                schedule = []


        #Main menu to allow for creating/editing/deleting/viewing tasks, exit program
        running = True
        while(running):
                #Display the options the user can make
                printMenu()
                #Prompt the user to make a choice, accept 0-5
                choice = input('What would you like to do? ')

                #Exit
                if choice == "0":
                        running = False
                        m.writeFile(saveFile, schedule)
                        break
                #Create Task
                elif choice == "1":
                        #Prompt user for task details and then add to schedule
                        schedule = m.addTask(m.newTask(), schedule)

                #Edit Task
                elif choice == "2":
                        #Prompt the user for the task to be modified
                        badTask = m.findTask(schedule)
                        if badTask != None:
                                m.editTask(badTask)
                        
                #Delete Task
                elif choice == "3":
                        #Prompt the user for the task to be deleted
                        badTask = m.findTask(schedule)                       
                        #Remove task from schedule
                        m.deleteTask(badTask, schedule)
                #View Task
                elif choice == "4":
                        #Prompt the user for the task to be viewed
                        print(v.viewTask(schedule))

                #View Schedule
                elif choice == "5":
                        v.viewSchedule(schedule)
                #Save Changes
                elif choice == "6":
                        m.writeFile(saveFile, schedule)
                        print("Saved.")
                #Invalid choice
                else:
                        print('Please choose a valid option.')


                #testTask = Task("test", "Transient", 1100, 100, 20220428, 20220429, 1)
                #testTask2 = Task("test2", "Recurring", 1111, 111, 20220428, 20220429, 1)


def printMenu():
        print('\nOptions:')
        print('1. New Task')
        print('2. Edit Task')
        print('3. Delete Task')
        print('4. View Task')
        print('5. View Schedule')
        print('6. Save Schedule')
        print('0. Exit Program')
        print()

if __name__ == '__main__':
	main()
