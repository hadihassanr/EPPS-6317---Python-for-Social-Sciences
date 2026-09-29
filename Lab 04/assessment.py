landuse = input("Land use type: ")
value = int(input("value: "))

if landuse == "SFR":
    rate = 0.05

elif landuse == "MFR":
    rate = 0.04

else:
    rate = 0.02

assessment = value * rate
print(assessment)
