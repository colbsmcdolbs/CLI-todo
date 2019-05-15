import sys
import functions

def main():
    args = sys.argv[1:]
    if len(args) < 1 or len(args) > 3:
        print('The incorrect number of arguments has been used.')
        functions.needHelp()
    
    # Displays the help screen
    if args[1] is "-help":
        functions.printHelp()

    # Displays list of all tasks.
    elif args[1] is "-v":
        functions.viewTasks()

    # Adds the task to Regular Tasks
    elif args[1] is "-a":
        if args[2]:
            functions.addTask(args[2])
            print('Your Task: {}'.format(args[2]))
            print('Has been added to your tasks.')
        else:
            print('Error, Incorrect Usage.')
            functions.needHelp()
    else:
        print('Error, idiot')
"""
    # Adds the task to MIT
    elif 

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
