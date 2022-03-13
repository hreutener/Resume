

import threading
import random
import time

def Philosopher(x,totalNumPhilosophers):
    plate = 100
    spot = x
    totalPhilo = totalNumPhilosophers
    haveLeft = False
    haveRight = False
    first = True
    print("P"+str(spot)+" is thinking...\n",end="")
    while(plate > 0):
        # think
        if(not first):
            print("P"+str(spot)+" pausing with "+str(plate)+" left.\n",end="")
        else:
            first=False
        time.sleep(random.uniform(0.2,0.6))
        if(spot%2==0):
            # pick up left fork
            forks[spot].pick_up()
            haveLeft = True
            time.sleep(0.01)
            print("P"+str(spot)+" taking left fork...\n",end="")

            # pick up right fork
            if(spot == totalPhilo-1):
                forks[0].pick_up()
            else:
                forks[spot+1].pick_up()
            haveRight = True
            time.sleep(0.01)
            print("P"+str(spot)+" taking right fork...\n",end="")
        else:
            # pick up right fork
            if(spot == totalPhilo-1):
                forks[0].pick_up()
            else:
                forks[spot+1].pick_up()
            haveRight = True
            time.sleep(0.01)
            print("P"+str(spot)+" taking right fork...\n",end="")

            # pick up left fork
            forks[spot].pick_up()
            haveLeft = True
            time.sleep(0.01)
            print("P"+str(spot)+" taking left fork...\n",end="")

        
        # eat
        print("P"+str(spot)+" is eating...\n",end="")
        time.sleep(random.uniform(0.2,0.6))
        amount = random.uniform(5, 10)
        plate -= amount

        # put right fork back
        if(spot == totalPhilo-1):
            forks[0].put_back()
        else:
            forks[spot+1].put_back()
        print("P"+str(spot)+" dropping right fork...\n",end="")
        haveRight = False

        # put left fork back
        forks[spot].put_back()
        print("P"+str(spot)+" dropping left fork...\n",end="")
        haveLeft = False
          
    print("P"+str(spot)+" is done!\n",end="")



            
class Fork:

    def __init__(self):
        self.lock = threading.Lock()

    def pick_up(self):
        self.lock.acquire()
    def put_back(self):
        self.lock.release()

philos = []
forks = []
data = int(input("Enter number of philosophers:"))
for i in range(data):
    forks.append(Fork())
for i in range(data):
    thread = threading.Thread(target=Philosopher, args=(i,data,))
    philos.append(thread)
    

for i in range(data):
    philos[i].start()

for i in range(data):
    philos[i].join()

print("All are done!")
                  
