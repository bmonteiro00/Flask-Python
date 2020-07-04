from app import app
from app.services.Services import GitService
from app.repository import GitRepository
from flask import Response


@app.route("/repository/user/<name>", methods=['GET'])
def list_repository_by_user(name):
    response = GitService(name).get_repository_by_username()
    document_id = GitRepository.save_document(response, name)
    return Response(document_id, mimetype="application/json", status=200)


@app.route("/repository/user/<name>/<reponame>",  methods=['GET'])
def list_single_repository_details(name, reponame):
    response = GitService(name, reponame).get_repository_details()
    document_id = GitRepository.save_document_details(response, reponame)
    return Response(document_id, mimetype="application/json", status=200)
