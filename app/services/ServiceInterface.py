import abc


class Service(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getrepositorybyusername(self, username):
        return

    @abc.abstractmethod
    def getrepository(self, username, reponame):
        return
