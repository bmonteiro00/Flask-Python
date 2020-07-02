from app import collection


def save_document(document):
    collection.insert(document)

