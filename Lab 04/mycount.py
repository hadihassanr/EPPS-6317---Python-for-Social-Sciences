import csv
def countnullfields(csvfilepath):
    count = 0
    with open(csvfilepath, 'r') as csvFile:
        reader = csv.reader(csvFile)
        headers = next(reader)

        for header in headers:
            if header == "":
                count =+ 1
    return count
    