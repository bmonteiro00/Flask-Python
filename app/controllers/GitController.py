from app import app
from app.models import GitModel
from app.services.Services import GitService
import json


@app.route("/repository/user/<name>", methods=['GET'])
def listrepositorybyuser(name):
    response = GitService(name).getrepositorybyusername()
    #document = json.loads(response)
    #GitModel.save_document(document)
    return response


@app.route("/repository/user/<name>/<reponame>",  methods=['GET'])
def listsinglerepository(name, reponame):
    response = GitService(name, reponame).getrepository()
    #GitModel.save_document(response)
    return response
