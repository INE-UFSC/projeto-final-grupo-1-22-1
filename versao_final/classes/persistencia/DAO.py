import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = []

        try:
            self.load()
        except FileNotFoundError:
            self.dump()

    def dump(self, filename: str = None):
        if filename == None:
            filename = self.__datasource
        pickle.dump(self.__cache, open(filename, 'wb'))

    def load(self, filepath: str = None):
        if filepath == None:
            filepath = self.__datasource
        self.__cache = pickle.load(open(filepath, 'rb'))

    def add(self, obj):
        self.__cache.append(obj)
        self.dump()

    def get_all(self):
        return self.__cache
