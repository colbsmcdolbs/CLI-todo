"""
These functions will dictate
all of the commands that can 
be submitted by a user.
Author: Colby Allen
"""
import json

yesAnswers = ['yes', 'y', 'yeah', 'yep','yessir', 'yeah', 'ya', 'yamon', 'yea']

def openJson(file):
    with open(file, 'r') as json_file:
        return json.load(json_file)

def writeJson(file, data):
    with open(file, 'w') as json_file:
        json.dump(data, json_file)

#TODO CREATE THE HELP
def printHelp():
    helpMessage = ""

def addTask(myTask):
    regLists = openJson('regTasks.json')
    regLists.append(myTask)
    writeJson('regTasks.json', regLists)

def addTaskMIT(myTask):
    mitLists = openJson('mitTasks.json')
    mitLists.append(myTask)
    writeJson('mitTasks.json', mitLists)

def viewTasks():
    mitLists = openJson('mitTasks.json')
    regLists = openJson('regTasks.json')
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
    mitLists = openJson('mitTasks.json')
    if mitLists:
        response = input('Do you really wish to delete all of your Most Important Tasks? [Y/n]')
        if response.lower() in yesAnswers:
            mitLists = []
            writeJson('mitTasks.json', mitLists)
            print('Your Most Import Task list has been cleared.')
        else:
            print('Alright, we won\'t erase that list.')
    else:
        print('It appears your Most Important Task list is already empty...')
        print('Nothing to do here.')
        

def deleteAllReg():
    regLists = openJson('regTasks.json')
    if regLists:
        response = input('Do you really wish to delete all of your Regular Tasks? [Y/n]')
        if response.lower() in yesAnswers:
            regLists = []
            writeJson('regTasks.json', regLists)
            print('Your Regular Task list has been cleared.')
        else:
            print('Alright, we won\'t erase that list.')
    else:
        print('It appears your Regular Task list is already empty...')
        print('Nothing to do here.')

def deleteAll():
    deleteAllMIT()
    deleteAllReg()





"""
def findTask(taskNum):


def completeTask(taskNum):
    print("Congrats on finishing task number {}.".format(taskNum))
    input = raw_input("Would you now like to delete task number {}? [Y/N]".format(taskNum))
    input.lower()
    if input in yesAnswers:
        deleteTask(taskNum)
    else:
        print("Alright, we won't delete it.")

def deleteTask(taskNum):
    
def deleteAll():
    
def deleteAllMIT():
    
def deleteAllReg():
    
"""