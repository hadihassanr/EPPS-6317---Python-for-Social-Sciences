import csv
import parcelclass
with open("parcels.csv", 'r') as parcels:
    reader = csv.reader(parcels)
    headers = next(reader)
    results = []
    for row in reader:
        myparcel = parcelclass.Parcel(row[1], int(row[2]))
        mytax = myparcel.assessment()
        results.append((row[0], mytax))
for item in results:
    # item [0] = FID
    # item [1] = tax
    print("FID", item[0], "has a tax value of", item[1])
    
