from app import app
from app.utils import HttpResponseConvert
from app.services.ServiceInterface import Service
import requests
import json


class GitService(Service):

    def __init__(self, username = None, repo_name = None):
        self.username = username
        self.repo_name = repo_name

    def get_repository_by_username(self):
        app.logger.debug('Calling getrepositorybyusername')
        host = "https://api.github.com/users/" + self.username + "/repos"
        r = requests.get(host)

        if r.status_code == requests.codes.ok:
            responses = json.loads(r.text)
            app.logger.debug('Successfull calling getrepository')
            return HttpResponseConvert.getresponseconvert(responses, 'name')
        else:
            return []

    def get_repository_details(self):
        app.logger.debug('Calling getrepository')
        host = "https://api.github.com/repos/" + self.username + "/" + self.repo_name
        r = requests.get(host)

        if r.status_code == requests.codes.ok:
            app.logger.debug('Successfull calling getrepository')
            return json.loads(r.text)
        else:
            return []
