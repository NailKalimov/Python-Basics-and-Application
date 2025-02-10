# Принцип инверсии зависимостей (Dependency Inversion Principle, DIP)
from abc import ABC, abstractmethod


# Abstract base class for a data source
class DataSource(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def write_data(self, data):
        pass


class TextDataSource(DataSource):
    def read_data(self):
        with open(self.path, 'r') as f:
            data = f.read()
        return data

    def write_data(self, data):
        with open(self.path, 'w') as f:
            f.write(data)


class DbDataSource(DataSource):
    def read_data(self):
        return "data from database"

    def write_data(self, data):
        print(f"write {data} to database")


class TextOperations:
    def __init__(self, data_source):
        self.data_source = data_source
        self.data = self.data_source.read_data()

    def search_for_word(self, word):
        return word in self.data

    def count_occurrences(self, word):
        return self.data.count(word)


file = TextDataSource("D:\\data.txt")
db = DbDataSource("customers")

obj = TextOperations(file)
print(f"{obj.search_for_word('more')}")
print(f"{obj.count_occurrences('be')}")

obj = TextOperations(db)
print(f"{obj.search_for_word('data')}")
print(f"{obj.count_occurrences('from')}")
