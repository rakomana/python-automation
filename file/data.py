import csv

with open("weather_data.csv") as data:
    values = list(csv.reader(data))

    temperatures = []

    for key in values:
        if key[1]  == 'temp':
            pass
        else:
            temperatures.append(int(key[1]))

print(temperatures)