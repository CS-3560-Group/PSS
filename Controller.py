'''
Controller is responsible for interaction with the user to 
the Viewer and Model
'''

from Task import Task
import Viewer as v
import Model as m
import traceback


def main():
    # Where to save schedule to
#     saveFile = "PSS_Schedule.json"
    # Variable to enable or disable debugging
    debug = False
    
    saveFile = printWelcome()
    print('Checking for existing schedule')

    # Try and load an existing schedule if there is one
    try:
        schedule = m.readFile(saveFile)
        print('Schedule found:')
        v.viewSchedule(schedule)
    except Exception:
        traceback.print_exc()
        print('No existing schedule found, creating a new one.')
        schedule = []

    # m.altWriteFile("daySchedule.json",schedule, 20220112,2)

    # Main menu to allow for creating/editing/deleting/viewing tasks, exit program
    running = True
    while(running):
        # Display the options the user can make
        printMenu()
        # Prompt the user to make a choice, accept 0-5
        choice = input('What would you like to do? ')

        # Exit
        if choice == "0":
            running = False
            f = input('Enter output file (include extension):')
            m.writeFile(f, schedule)
            break
        # Create Task
        elif choice == "1":
            # Prompt user for task details and then add to schedule
            schedule = m.addTask(m.newTask(), schedule)

        # Edit Task
        elif choice == "2":
            # Prompt the user for the task to be modified
            badTask = m.findTask(schedule)
            if badTask != None:
                m.editTask(badTask)

        # Delete Task
        elif choice == "3":
            # Prompt the user for the task to be deleted
            badTask = m.findTask(schedule)
            # Remove task from schedule
            m.deleteTask(badTask, schedule)
        # View Task
        elif choice == "4":
            # Prompt the user for the task to be viewed
            print(v.viewTask(schedule))

        # View Schedule
        elif choice == "5":
            v.viewSchedule(schedule)
        # Save Changes
        elif choice == "6":
            printWrite()
            opt = int(input())
            while opt != 1 and opt != 2 and opt != 3 and opt != 4:
                print('Please choose a valid option.')
                printWrite()
                opt = int(input())

            f = input('Enter output file (include extension):')

            if opt == 4:
                m.writeFile(f, schedule)
            else:
                d = int(input('Enter start date (yyyymmdd):'))
                m.altWriteFile(f, schedule, d, opt)

            print("Saved.")
        # Invalid choice
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


def printWrite():
    print('How would you like to write the schedule?')
    print('\nOptions:')
    print('1. Day')
    print('2. Week')
    print('3. Month')
    print('4. Entire Scheduled')

def printWelcome():
    opt = -1
    print('Welcome to PSS')
    while opt != 1 and opt != 2:
        print('What file will you load?')
        print('1. Default schedule (PSS_Schedule.json)')
        print('2. Custom schedule')
        opt = int(input())
        print()
    if opt == 1:
            return 'PSS_Schedule.json'
    else:
            return input('Enter file name with extension:')


if __name__ == '__main__':
    main()
