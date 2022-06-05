import zmq
import ast
import pymongo

cluster = pymongo.MongoClient("mongodb+srv://osman:567890123@cluster0.wad24.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["db_proje"]
mycol = db["marker"]

ctx = zmq.Context()
sock = ctx.socket(zmq.SUB)
sock.connect("tcp://127.0.0.1:1234")
sock.subscribe("") # Subscribe to all topics
sozliste =[]

say=0

print("Starting receiver loop ...")
while True:
    
    if(say<4688):
        
        while(say<4688):
            msg = sock.recv_string()

            mesaj2=ast.literal_eval(str(msg))
            print(mesaj2)
        
            sozliste.append(mesaj2)
            say+=1
        
        mycol.insert_many(sozliste)
    
    print("---------------------------------------")
    msg = sock.recv_string()
    mesaj2=ast.literal_eval(str(msg))
    mycol.insert_one(mesaj2)
    print(mesaj2)