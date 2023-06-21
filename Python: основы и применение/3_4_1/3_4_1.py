from csv import DictReader
from collections import Counter
from time import strptime, struct_time

crimes = []
with open("Crimes.csv", "r") as file:
    reader = DictReader(file)
    for row in reader:
        if  strptime(row['Date'], "%m/%d/%Y %H:%M:%S %p").tm_year == 2015:
            crimes.append(row['Primary Type'])
c = Counter(crimes).most_common()
print(c[0])
