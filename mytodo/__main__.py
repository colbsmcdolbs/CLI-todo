from sys import argv
import functions
import numbers

def main():
    
    if len(argv) < 1 or len(argv) > 4:
        print('The incorrect number of arguments has been used.')
        print('Error, incorrect usage.')
    
    # Displays the help screen
    if argv[1] == "-help":
        functions.printHelp()

    # Displays list of all tasks.
    elif argv[1] == "-v":
        functions.viewTasks()

    # Completes the task then asks user if they wish to delete it.
    elif argv[1] == "-c":
        try:
            num = int(argv[2])
            functions.completeTask(num)
        except IndexError:
            print('Error, Incorrect Usage.')

    # Adds the task to a task list
    elif argv[1] == "-a":
        try:
            if argv[2] == "-mit":
                try:
                    functions.addTaskMIT(argv[3])
                except IndexError:
                    print('Error, Incorrect Usage.')
            else: 
                functions.addTask(argv[2])
        except IndexError:
            print('Error, Incorrect Usage.')
    
    # Handles the deleting function
    elif argv[1] == "-d":
        if argv[2] == "-all":
            functions.deleteAll()
        elif argv[2] == "-mit":
            functions.deleteAllMIT()
        elif argv[2] == "-reg":
            functions.deleteAllReg()
        else:
            try:
                num = int(argv[2])
                functions.deleteTask(num)
            except:
                print('Error, Incorrect Usage.')
    else:
        print('Error, command not understood.')

if __name__ == '__main__':
    main()
