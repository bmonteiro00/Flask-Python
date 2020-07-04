from app import db, app
from app.models.GitModels import GitRepoModel, GitRepoDetailsModel


def save_document(response, owner):
    collection = db.git
    document = GitRepoModel(_id=owner, repo_title=response)
    result = collection.insert_one(document.to_mongo())
    app.logger.debug('Successfully inserted document with id = ' + result.inserted_id)
    return result.inserted_id


def save_document_details(response, repo_name):
    collection = db.git_details
    document = GitRepoDetailsModel(_id=repo_name, repo_details=response)
    result = collection.insert_one(document.to_mongo())
    app.logger.debug('Successfully inserted document details with id = ' + result.inserted_id)
    return result.inserted_id
