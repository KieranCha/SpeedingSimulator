import random as r
carExampleObject = {
    "Brand": "placeholder",
    "Model": "placeholder",
    "Year": "placeholder"
    }

exampleBrands = ["Swardine","Drawning","Iounine","Plonk","Ronari","Youcar"]
exampleModels = ["Sword","Conquer","Saviour","Economic","20EF","Throug","Traveller","Jungle","Klerk","Timesave"]
exampleForenames = ["Drake", "Loyld", "Jackson", "Kieran", "Aaron", "Klurk", "Werold", "Harold", "Hagrid", "Joseph", "Kenzie", "Alex", "Max"]
exampleSurnames = [" Nurak", " Goldridden", " the Fortunate", " Carok", " Von Sulver", " Royal", " Chalmers"]

with open("policeCarDatabase.txt", 'w') as carDB:
    carDBdict  = {}
    for x in range(100):
        licensePlate = chr(r.randint(65,90)) + chr(r.randint(65,90)) + str(r.randint(0,9)) + str(r.randint(0,9)) + " " + chr(r.randint(65,90)) + chr(r.randint(65,90)) + chr(r.randint(65,90))
        carDBdict[licensePlate] = {}
        carDBdict[licensePlate]["car"] = {}
        carDBdict[licensePlate]["car"]["brand"] = r.choice(exampleBrands)
        carDBdict[licensePlate]["car"]["model"] = r.choice(exampleModels)
        carDBdict[licensePlate]["car"]["year"] = r.randint(1979, 2030)

        carDBdict[licensePlate]["owner"] = r.choice(exampleForenames) + r.choice(exampleSurnames)
        
        carDBdict[licensePlate]["previousFines"] = {}

        print(licensePlate)
        print(carDBdict[licensePlate]["owner"])
        print(carDBdict[licensePlate]["car"])
        print("")
    carDB.write(str(carDBdict))
        


