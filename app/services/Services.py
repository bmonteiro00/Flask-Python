from app import app
from app.utils import HttpResponseConvert
from app.services.ServiceInterface import Service
import requests
import json


class GitService(Service):

    def __init__(self, username = None, reponame = None):
        self.username = username
        self.reponame = reponame

    def getrepositorybyusername(self):
        app.logger.debug('Calling getrepositorybyusername')
        host = "https://api.github.com/users/" + self.username + "/repos"
        r = requests.get(host)

        if r.status_code == requests.codes.ok:
            responses = json.loads(r.text)
            app.logger.debug('Successfull calling getrepository')
            return json.dumps(HttpResponseConvert.getresponseconvert(responses, 'name'))
        else:
            return "error"

    def getrepository(self):
        app.logger.debug('Calling getrepository')
        host = "https://api.github.com/repos/" + self.username + "/" + self.reponame
        r = requests.get(host)

        if r.status_code == requests.codes.ok:
            app.logger.debug('Successfull calling getrepository')
            return json.loads(r.text)
        else:
            return "error"
