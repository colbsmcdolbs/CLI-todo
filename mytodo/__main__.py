from sys import argv
import functions

def main():
    
    if len(argv) < 1 or len(argv) > 4:
        print('The incorrect number of arguments has been used.')
        functions.printHelp()
    
    # Displays the help screen
    if argv[1] == "-help":
        functions.printHelp()

    # Displays list of all tasks.
    elif argv[1] == "-v":
        functions.viewTasks()

    # Adds the task to a task list
    elif argv[1] == "-a":
        try:
            if argv[2] == "-mit":
                try:
                    functions.addTaskMIT(argv[3])
                    print('Your Task: {}'.format(argv[3]))
                    print('Has been added to your Most Important Tasks.')
                except IndexError:
                    print('Error, Incorrect Usage.')
                    functions.printHelp()
            else: 
                functions.addTask(argv[2])
                print('Your Task: {}'.format(argv[2]))
                print('Has been added to your tasks.')
        except IndexError:
            print('Error, Incorrect Usage.')
            functions.printHelp()
    # Handles the deleting function
    elif argv[1] == "-d":
        if argv[2] == "-all":
            functions.deleteAll()
        elif argv[2] == "-mit":
            functions.deleteAllMIT()
        elif argv[2] == "-reg":
            functions.deleteAllReg()
        else:
            print('Error, Incorrect Usage.')

    else:
        print('Error, idiot')
"""

    # Completes the task and Asks user if they want to remove it
    elif args[1] is "-d":

        # Deletes task specified
        if args[2].is_integer():
            

        # Deletes all tasks
        if args[2] is "-all":


        # Deletes all MIT Tasks
        if args[2] is "-all-mit":


        # Deletes all Regular Tasks
        if args[2] is "-all-reg":
    
"""
if __name__ == '__main__':
    main()
