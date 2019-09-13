def updateCsv(fileName, passengerId, pClass, name, sex, age, sibSp, parch, ticket, fare, cabin, embarked):
    inputFile = open(fileName, "a")    # OppeningFile
    inputFile.write("Primeira,Segunda\n")   # Appending Lines

# Test Procedure
updateCsv("TestCSV.csv","","","","","","","","","","","")

# Test Verification
f = open("TestCSV.csv", "r")
print(f.read())
