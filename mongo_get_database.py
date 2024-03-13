from pymongo import MongoClient


def get_database():
    connection_string = ("mongodb://gen_user:141Plazakash@82.97.244.15:27017/colizeum_db?authSource=admin"
                         "&directConnection=true")
    client = MongoClient(connection_string)
    return client['colizeum_db']
