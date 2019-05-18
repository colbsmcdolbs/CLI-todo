"""
These functions will dictate
all of the commands that can 
be submitted by a user.
Author: Colby Allen
"""
import json
from pathlib import Path

yesAnswers = ['yes', 'y', 'yeah', 'yep','yessir', 'yeah', 'ya', 'yamon', 'yea']
path = Path(__file__).parent.absolute()

def openJson(file):
    with open(file, 'r') as json_file:
        return json.load(json_file)

def writeJson(file, data):
    with open(file, 'w') as json_file:
        json.dump(data, json_file)

def addTask(myTask):
    regLists = openJson(str(path) + '/regTasks.json')
    regLists.append(myTask)
    writeJson(str(path) + '/regTasks.json', regLists)
    print('Your Task: {}'.format(myTask))
    print('Has been added to your tasks.')

def addTaskMIT(myTask):
    mitLists = openJson(str(path) + '/mitTasks.json')
    mitLists.append(myTask)
    writeJson(str(path) + '/mitTasks.json', mitLists)
    print('Your Task: {}'.format(myTask))
    print('Has been added to your Most Important Tasks.')

def viewTasks():
    mitLists = openJson(str(path) + '/mitTasks.json')
    regLists = openJson(str(path) + '/regTasks.json')
    index = 1
    print('============================')
    if mitLists:
        print('Most Important Tasks:')
        for task in mitLists:
            print("{}. {}".format(index, task))
            index += 1
        print('\n')
    if regLists:
        print('Regular Tasks:')
        for task in regLists:
            print("{}. {}".format(index, task))
            index += 1
    print('============================')

def deleteAllMIT():
    mitLists = openJson(str(path) + '/mitTasks.json')
    if mitLists:
        response = input('Do you really wish to delete all of your Most Important Tasks? [Y/n]')
        if response.lower() in yesAnswers:
            mitLists = []
            writeJson(str(path) + '/mitTasks.json', mitLists)
            print('Your Most Import Task list has been cleared.')
        else:
            print('Alright, we won\'t erase that list.')
    else:
        print('It appears your Most Important Task list is already empty...')
        print('Nothing to do here.')
        

def deleteAllReg():
    regLists = openJson(str(path) + '/regTasks.json')
    if regLists:
        response = input('Do you really wish to delete all of your Regular Tasks? [Y/n]')
        if response.lower() in yesAnswers:
            regLists = []
            writeJson(str(path) + '/regTasks.json', regLists)
            print('Your Regular Task list has been cleared.')
        else:
            print('Alright, we won\'t erase that list.')
    else:
        print('It appears your Regular Task list is already empty...')
        print('Nothing to do here.')

def deleteAll():
    deleteAllMIT()
    deleteAllReg()

def completeTask(taskNum):
    if checkValidTaskNum(taskNum):
        print("Congrats on finishing task number {}.".format(taskNum))
        response = input("Would you now like to delete task number {}? [Y/N]".format(taskNum))
        response = response.lower()
        if response in yesAnswers:
            deleteTask(taskNum)
        else:
            print("Alright, we won't delete it.")
    else:
        print('Invalid usage. Retry after verifying your task number.')


def deleteTask(taskNum):
    if checkValidTaskNum(taskNum):
        response = input('Do you really wish to remove task number {}? [Y/n]'.format(taskNum))
        response = response.lower()
        if response in yesAnswers:
            mitLists = openJson(str(path) + '/mitTasks.json')
            regLists = openJson(str(path) + '/regTasks.json')
            index = 1
            isDeleted = False
            for idx, task in enumerate(mitLists):
                if taskNum == index:
                    deleted = task
                    mitLists.pop(idx)
                    writeJson(str(path) + '/mitTasks.json', mitLists)
                    isDeleted = True
                    break
                index += 1
            if not isDeleted:
                for idx, task in enumerate(regLists):
                    if taskNum == index:
                        deleted = task
                        regLists.pop(idx)
                        writeJson(str(path) + '/regTasks.json', regLists)
                        break
                    index += 1
            print('Your task "{}" has been deleted.'.format(deleted))
        else:
            print('Alright, we won\'t delete that for you.')
    else:
        print('Invalid usage. Retry after verifying your task number.')

def checkValidTaskNum(taskNum):
    mitLists = openJson(str(path) + '/mitTasks.json')
    regLists = openJson(str(path) + '/regTasks.json')
    numTasks = len(mitLists) + len(regLists)
    if mitLists or regLists:
        if 1 <= taskNum <= numTasks:
            return True
        else:
            return False
    else:
        return False

def printHelp():
    helpMessage = "Instructions on how to use mytodo:\n"
    helpMessage += "To Add a Task to Regular List:\n"
    helpMessage += "Command: mytodo -a <'Your task in quotes'>\n\n"
    helpMessage += "To Add a Task to Your Most Important Task List:\n"
    helpMessage += "Command: mytodo -a -mit <'Your task in quotes'>\n\n"
    helpMessage += "To View All of Your Current Tasks:\n"
    helpMessage += "Command: mytodo -v\n\n"
    helpMessage += "To Complete a Task(Find Task Number by Using the View Command):\n"
    helpMessage += "Command: mytodo -c <Your Task Number as an Integer>"
    helpMessage += "To Delete a Specific Task (Find Task Number by Using the View Command):\n"
    helpMessage += "Command: mytodo -d <Your Task Number as an integer>\n\n"
    helpMessage += "To Delete All Tasks From Both Lists:\n"
    helpMessage += "Command mytodo -d -all\n\n"
    helpMessage += "To Delete All From Certain List(-mit for Most Important or -reg for Regular):\n"
    helpMessage += "Command mytodo -d <-mit or -reg>"
    print(helpMessage)