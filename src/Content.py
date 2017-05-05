import requests
import json

class Content(object):
    
    def __init__(self):
        self.url = 'http://vca.informatik.hu-berlin.de/dispenser/test'
        self.jsonPath = '../res/json/'

    def getHtmlContentByRequest(self, jsonName):
        fullJsonPath = self.jsonPath + jsonName + '.txt'
        with open(fullJsonPath) as json_file:
            templateJson = json.load(json_file)
            req = requests.post(self.url, json=templateJson)
            print(req.text)
        return req.text


