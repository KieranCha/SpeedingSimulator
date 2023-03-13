#IMPORTS
import random as r
from datetime import datetime


#FUNCTIONS
def simRoadDay():
    cars = []
    speedingCars = []
    for car in range(r.randint(4,20)):
        cars.append(r.choice(licensePlates))
    for hours in range(12):
        passingCar = r.choice(cars)
        passingCarSpeed = r.randint(40,70)
        if passingCarSpeed > 60:
            speedingCars.append(passingCar)
    return speedingCars
        
def saveChanges():
    with open("policeCarDatabase.txt",'w') as saveCarDB:
        saveCarDB.write(str(policeDB))


#MAIN
with open("policeCarDatabase.txt",'r') as carDB:
        policeDB = eval(carDB.read())
        licensePlates = list(policeDB.keys())

currentDay = datetime.now().strftime("%d/%m/%Y")
speedLimit = 60
roadDistance = 30 #Miles
#speed = distance / speed

daycount = 0
while True:
    daycount += 1
    speeders = simRoadDay()
    print("Day ", str(daycount))
    if speeders == []:
        print("No speeders\n")
        input()
        continue
    else:
        print(str(len(speeders)), "speeders\n")
        for speeder in speeders:
            print("Offender:",policeDB[speeder]["owner"])
            print("Car:",str(policeDB[speeder]["car"]["year"]) + " ", policeDB[speeder]["car"]["brand"] + " ", policeDB[speeder]["car"]["model"])
            print("Previous fines? ", "None" if policeDB[speeder]["previousFines"] == [] else str(len(policeDB[speeder]["previousFines"])))
            for fineDate in policeDB[speeder]["previousFines"].keys():
                print(fineDate, policeDB[speeder]["previousFines"][fineDate])

            print("\n")
            policeDB[speeder]["previousFines"][currentDay] = "£" + str(r.randint(1000,14000)) 
            saveChanges()

    input()
            
            
