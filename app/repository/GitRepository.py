from app import db, app
from app.models.GitModels import GitRepoModel, GitRepoDetailsModel


def save_document(response, owner):
    collection = db.git
    document = GitRepoModel(_id=owner, repo_title=response)
    result = collection.replace_one(filter={'_id':owner}, replacement = document.to_mongo(), upsert = True)

    if result.modified_count:
        app.logger.debug('Successfully inserted new document with id = ' + result.upserted_id )
        document_id = result.upserted_id
    else:
        app.logger.debug('Successfully updated document with id = ' + owner )
        document_id = owner
    return document_id


def save_document_details(response, repo_name):
    collection = db.git_details
    document = GitRepoDetailsModel(_id=repo_name, repo_details=response)
    result = collection.replace_one(filter={'_id': repo_name}, replacement=document.to_mongo(), upsert=True)

    if result.modified_count:
        app.logger.debug('Successfully inserted new document with id = ' + result.upserted_id)
        document_id = result.upserted_id
    else:
        app.logger.debug('Successfully updated document with id = ' + repo_name)
        document_id = repo_name

    return document_id
