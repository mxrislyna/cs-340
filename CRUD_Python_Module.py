from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Connection Variables
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        
        # Initialize Connection using MongoDB URI with authentication
        self.client = MongoClient('mongodb://%s:%s@%s:%d/?authSource=admin' % (USER, PASS, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Method to implement the C (Create) in CRUD
    def create(self, data):
        if data is not None:
            try:
                # Insert the document into the collection
                result = self.collection.insert_one(data)
                
                # Check if insert was acknowledged and return boolean
                if result.acknowledged:
                    return True
                else:
                    return False
            except Exception as e:
                print("Insert failed:", e)
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Method to implement the R (Read) in CRUD
    def read(self, query):
        if query is not None:
            try:
                # Use find() to get the cursor, then convert cursor to a list
                cursor = self.collection.find(query)
                return list(cursor)
            except Exception as e:
                print("Query failed:", e)
                return []
        else:
            raise Exception("Nothing to search, because query parameter is empty")
            
    # Method to implement the U (Update) in CRUD
    def update(self, query, update_data):
        if query is not None and update_data is not None:
            try:
                # Use update_many to update all matching documents, or update_one for a single document
                result = self.collection.update_many(query, { "$set": update_data })
                
                # Return the count of modified documents
                return result.modified_count
            except Exception as e:
                print("Update failed:", e)
                return 0
        else:
            raise Exception("Parameters are empty, nothing to update")
            
    # Method to implement the D (Delete) in CRUD
    def delete(self, query):
        if query is not None:
            try:
                # Use delete_many to remove all matching documents, or delete_one for a single document
                result = self.collection.delete_many(query)
                
                # Return the count of deleted documents
                return result.deleted_count
            except Exception as e:
                print("Delete failed:", e)
                return 0
        else:
            raise Exception("Parameters are empty, nothing to delete")