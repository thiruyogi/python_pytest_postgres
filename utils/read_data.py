import csv
def getCSVData(fileName):
    #create an empty list to store rows
    rows = []
    # open the CSV file
    dataFile = open(fileName, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(dataFile)
    # skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
    # data =[]
    # with open(fileName, 'r') as file:
    #     csv_reader = csv.DictReader(file)
    #     data = [row for row in csv_reader]
    # return(data)
