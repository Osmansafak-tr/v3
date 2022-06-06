import pymongo

cluster = pymongo.MongoClient("<YOUR MONGODB CONNECTİON STRİNG>")
db = cluster["db_proje"]
mycol = db["marker"]

mycol.delete_many({})
#x = mycol.find()

#x = mycol.find({'Araba':{'$in':['47','52']}})
#x = mycol.find({'Araba':'47'},{'_id': False}).sort('_id',-1).limit(30)



