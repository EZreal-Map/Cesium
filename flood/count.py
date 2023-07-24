def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) == 3:
                data.append(float(values[2]))
    return data

def count_values(data, num_intervals=10):
    interval_size = 10 / num_intervals
    value_counts = [0] * num_intervals
    
    for value in data:
        if 0 <= value <= 10:
            interval_index = int(value / interval_size)
            value_counts[interval_index] += 1

    return value_counts

if __name__ == "__main__":
    file_path = "clearcenter1.txt"
    data = read_data(file_path)
    value_counts = count_values(data)
    total_data = len(data)
    
    for i, count in enumerate(value_counts):
        lower_bound = i * (10 / 20)
        upper_bound = (i + 1) * (10 / 20)
        percentage = (count / total_data) * 100
        print(f"Range: [{lower_bound:.1f}, {upper_bound:.1f}), Count: {count}, Percentage: {percentage:.2f}%")
