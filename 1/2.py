with open("input", 'r') as f:
    measurements = [int(measurement) for measurement in f.read().splitlines()]

window_size = 3
window = []
previous_total = float('inf')
increase_counter = 0

for measurement in measurements:
    window.append(measurement)
    if len(window) < window_size:
        continue
    window = window[-window_size:]
    current_total = sum(window)
    if current_total > previous_total:
        increase_counter += 1
    previous_total = current_total

print(increase_counter)