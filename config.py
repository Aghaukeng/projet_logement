from pymongo import MongoClient
def get_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logements_sociaux_DB']
    return db,client