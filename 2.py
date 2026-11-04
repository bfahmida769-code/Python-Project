readings=[21.5,None,24.0,31.2,-4.0,28.5,None,35.1]
clean_readings=[]
alerts=[]

for reading in readings:
    if reading is None:
        continue
    if reading<0 or reading>50:
        continue

    clean_readings.append(reading)
    if reading>30:
        alerts.append(reading)
average=sum(clean_readings)/len(clean_readings)

print("clean readings: ",clean_readings)
print(f"Average: {average:.2f}")
print("Alerts: ",alerts)
