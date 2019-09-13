import csv
import os
#import pandas as pd

#def appendNewPerson(fileName, passengerId, pClass, name, sex, age, sibSp, parch, ticket, fare, cabin, embarked):
#    pd.read_csv(fileName)

# This function will append a line to a CSV File
def appendNewPerson(fileName, passengerId, pClass, name, sex, age, sibSp, parch, ticket, fare, cabin, embarked):
    inputFile = open(fileName, "a")    # Oppening File
    inputFile.write(passengerId + "," + pClass + "," + name + "," + sex + "," + age + "," + sibSp + "," + parch + "," + ticket + "," + fare + "," + cabin + "," + embarked)   # Appending Lines
    inputFile.write("\n")
    #inputFile.write("Primeira{},Segunda{}\n".format("3","3"))   # Appending Lines
    inputFile.close()

# This function will update a field in a CSV file
#def updateCsv(fileName, rowIndex, coloumnIndex, ):


# Test
#appendNewPerson("TestCSV.csv","passengerId","pClass","name","sex","age","sibSp","parch","ticket","fare","cabin","embarked")
#f = open("TestCSV.csv", "r")
#print(f.read())
#f.close()