import sys
import functions

def main()
    args = sys.argv[1:]
    if args < 2 or args > 3:
        print('The incorrect number of arguments has been used.')
        functions.needHelp()
    
    # Displays the help screen
    if args[1] is "-help":
        functions.printHelp()
    # Displays list of all tasks.
    elif args[1] is "-v":
        functions.viewTasks()
    elif args[1] is "-a":
        if args[2]:
            functions.addTask(args[2])
            print('Your Task: {}'.format(args[2]))
            print('Has been added to your tasks.')
        else:
            print('Error, Incorrect Usage.')
            functions.needHelp()
        

if __name__ == '__main__':
    main()