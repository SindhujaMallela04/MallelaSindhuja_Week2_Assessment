from abc import ABC, abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Inserting data into SQL Database.")
    
    def update(self):
        print("Updating data into SQL Database.")
    
    def delete(self):
        print("Deleting data from SQL Database.")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("Inserting data into NoSQL Database.")
    
    def update(self):
        print("Updating data into NoSQL Database.")
    
    def delete(self):
        print("Deleting data from NoSQL Database.")
    
def main():
    sql_database = SQLDatabase()
    sql_database.insert()
    sql_database.update()
    sql_database.delete()
    
    nosql_database = NoSQLDatabase()
    nosql_database.insert()
    nosql_database.update()
    nosql_database.delete()
main()
