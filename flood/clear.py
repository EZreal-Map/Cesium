#  清除

def read_and_filter_data(input_file, output_file, threshold):
    kept_data = []
    deleted_data = []

    with open(input_file, 'r') as f:
        lines = f.readlines()

        for line in lines:
            data = line.strip().split(',')
            if len(data) == 3:
                try:
                    value = float(data[2])
                    if value > threshold:
                        kept_data.append(line)
                    else:
                        deleted_data.append(line)
                except ValueError:
                    print(f"Error: Invalid data format in line: {line}")

    with open(output_file, 'w') as f:
        f.writelines(kept_data)

    return len(deleted_data), len(kept_data), kept_data


input_file = "center1.txt"
output_file = "clearcenter1.txt"
threshold = 0.1

deleted_count, kept_count, kept_data = read_and_filter_data(input_file, output_file, threshold)

deleted_percentage = deleted_count / (deleted_count + kept_count) * 100
kept_percentage = kept_count / (deleted_count + kept_count) * 100

print(f"Deleted rows: {deleted_count:<5}   {deleted_percentage:.2f}%")
print(f"Kept rows:    {kept_count:<5}   {kept_percentage:.2f}%")