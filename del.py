import pymongo

cluster = pymongo.MongoClient("mongodb+srv://osman:567890123@cluster0.wad24.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["db_proje"]
mycol = db["marker"]

mycol.delete_many({})
#x = mycol.find()

#x = mycol.find({'Araba':{'$in':['47','52']}})
#x = mycol.find({'Araba':'47'},{'_id': False}).sort('_id',-1).limit(30)



