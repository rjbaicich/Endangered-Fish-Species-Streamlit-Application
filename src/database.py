from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connect_to_mongodb():
    uri = "mongodb+srv://Radmin:<JFSCNrf5HOgg6dZD>@endangeredfish.bkd2bc1.mongodb.net/"

    #Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    #Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client  #Return the MongoDB client object
    except Exception as e:
        print(e)
        return None  #Return None if the connection failed
