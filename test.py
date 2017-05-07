import csv
while True:
    operation = raw_input("\nEnter an operation. F = add fish, L = view log, and E = end.: ")
    
    if operation == 'F':
        species = raw_input("\nWhat is the species?: ")
        temp = raw_input("What is the air temperature?: ")
        baro = raw_input("What is the barometric pressure?: ")
        humid = raw_input("What is the humidity?: ")
        appendMe = '\n'+species+','+temp+','+baro+','+humid
        appendFile = open('testLog.csv', 'a')
        appendFile.write(appendMe)
        appendFile.close()


    elif operation == 'L':
        with open('testLog.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row)

    elif operation == 'E':
        break

    else:
        print ('\nInvalid operation')
