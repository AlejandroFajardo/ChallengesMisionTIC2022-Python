import csv

archivo = open("GOOG.csv", mode = "r")
reader = csv.DictReader(archivo)

listaProm = []
for fila in reader:
    prom = ((float(fila["High"])+ float(fila["Low"]))/2)
    listaProm.append(prom)

highest_mean = float(max(listaProm))
lowest_mean = float(min(listaProm))

a = listaProm.index(max(listaProm))
b = listaProm.index(min(listaProm))

date_highest_mean = ""
date_lowest_mean = ""
#print (a, b)

for fila in reader:
    if fila == a:
        date_highest_mean = (fila["Date"])
    if fila == b:
        date_lowest_mean = (fila["Date"])
        
print("============================")
#print(listaProm)
print("_______________________________")
print(highest_mean)
print("_______________________________")
print(lowest_mean)
print("_______________________________")
print(a)
print("_______________________________")
print(b)