import csv
streetsCSV = "streets.csv"

def listheadernames(csvfilepath):
    # we will move the csv reading code into this function
    with open(csvfilepath, 'r') as csvFile:

        reader = csv.reader(csvFile)
        headers = next(reader)
    # Creat a list to save headers
    headerlist = []
    for header in headers:
        headerlist.append(header)
    return headerlist


    
