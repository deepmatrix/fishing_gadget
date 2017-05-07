import csv
with open('testLog.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        
#leave anything above this alone
        
    speciesL = []
    tempL = []
    baroL = []
    humidL = []
    for row in readCSV:
        species = row[0]
        temp = row[1]
        baro = row[2]
        humid = row[3]

        speciesL.append(species)
        tempL.append(temp)
        baroL.append(baro)
        humidL.append(humid)

    print(speciesL)
    print(tempL)
    print(baroL)
    print(humidL)
