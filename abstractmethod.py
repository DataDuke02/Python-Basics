from abc import ABC, abstractmethod

class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    def run_query(self, query):   # concrete method
        self.connect()
        result = self.execute(query)
        self.disconnect()
        return result

class MySQLConnector(DatabaseConnector):
    def connect(self):
        return "Connected to MySQL"

    def execute(self, query):
        return f"MySQL executing: {query}"

    def disconnect(self):
        return "MySQL disconnected"

class MongoConnector(DatabaseConnector):
    def connect(self):
        return "Connected to MongoDB"

    def execute(self, query):
        return f"MongoDB executing: {query}"

    def disconnect(self):
        return "MongoDB disconnected"

db = MySQLConnector()
print(db.run_query("SELECT * FROM users"))
