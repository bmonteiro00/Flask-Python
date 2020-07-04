from mongoengine import (
    StringField,
    ListField,
    DictField,
    Document
)


class GitRepoModel(Document):
    _id = StringField(required=True, max_length=200)
    repo_title = ListField()


class GitRepoDetailsModel(Document):
    _id = StringField(required=True, max_length=200)
    repo_details = DictField(required=True)
