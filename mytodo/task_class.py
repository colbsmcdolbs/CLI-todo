"""
This class will attempt
to read information from
the json file when it is
instantiated and populate 
the users tasks that had
previously been added.

Author: Colby Allen
"""
import json


class taskLists():
    def __init__(self)
        with open('mitTasks.json') as json_file:
            self.mitList = json.load(json_file)
        with open('regTasks.json') as json_file:
            self.regLists = json.load(json_file)