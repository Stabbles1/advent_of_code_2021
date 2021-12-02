with open("src/day_1/input", 'r') as f:
    measurements = [int(measurement) for measurement in f.read().splitlines()]


increase_counter = 0
previous_measurement = float('inf')

for measurement in measurements:
    if measurement > previous_measurement:
        increase_counter += 1
    previous_measurement = measurement

print(increase_counter)
