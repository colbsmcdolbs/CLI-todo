"""
These functions will dictate
all of the commands that can 
be submitted by a user.
Author: Colby Allen
"""
import json

yesAnswers = ['yes', 'y', 'yeah', 'yep','yessir']

def openJson(file):
    with open(file, 'r') as json_file:
        return json.load(file)

def writeJson(file, data):
    with open(file, 'w') as json_file:
        data = json.dump(data, json_file)

#TODO CREATE THE HELP
def printHelp():
    print('This Will print help.')

def addTask(myTask):
    reglists = openJson(regTasks)
    regLists.append(myTask)
    writeJson(regTasks, reglists)
    print("Item successfully added to Regular Tasks.")
"""
def addTaskMIT(myTask):
    mitLists = openJson(mitTasks)
    mitLists.append(myTask)
    writeJson(mitTasks, mitLists)
    print("Item successfully added to Most Important Tasks.")

def viewTasks():
    mitLists = openJson(mitTasks)
    regLists = openJson(regTasks)
    index = 1
    if mitLists:
        for task in mitLists:
            print("{}. {}".format(index, task))
            index += 1
    if regLists:
        for task in regLists:
            print("{}. {}".format(index, task))
            index += 1

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
    
def printHelp():
    
def needHelp():
    print('Please use "mytodo -help" for a list of commands.')  
"""
