import zmq
import time
import csv

ctx = zmq.Context()
sock = ctx.socket(zmq.PUB)
sock.bind("tcp://*:1234")







file = open("güncelzaman.csv")
csvreader = csv.reader(file)
header = next(csvreader)


liste = []
rows = []
for row in csvreader:
    rows.append(row)
file.close()



başlık = ["Zaman", "X", "Y", "Araba"]





for i in rows:
    sözlük = dict(zip(başlık, i))
    liste.append(sözlük)
    

print("uyu 2 sn")
time.sleep(2)
print("uyan")




sondort=4688



print("Starting loop...")
m=0


while(1):
    
    
    
    
    
    if m<4688:

        msg = str(liste[m])
        sock.send_string(msg)
        print("-> %s"% msg)
        m+=1
        
        
    else:
        print("\n>>>\n>>>\n>>>\n")
        k=0
        l=0
        print("0",sondort)
        while(l<30):
            print("+++++++++++++++++++++++++++++++++++++++")
            
            while(k<4):
                
                
                if liste[sondort]["Zaman"]==liste[sondort+1]["Zaman"]:
                    msg = str(liste[sondort])
                    sock.send_string(msg)
                    print("-> %s"% msg)
                    sondort+=1
                
                else:
                    msg = str(liste[sondort])
                    sock.send_string(msg)
                    print("-> %s"% msg)

                    break
                k+=1
                
            sondort+=1    
            l+=1
            k=0
            time.sleep(3)