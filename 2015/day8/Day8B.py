import re

def calculate_encoded_difference(filename):
    total_raw = 0
    total_encoded = 0

    with open(filename, "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            # Raw length: the string itself with quotes and escape sequences
            raw_length = len(line)
            total_raw += raw_length

            # Encoded length: after escaping the quotes and backslashes
            # The encoding should escape `"` and `\` by adding a backslash before them
            encoded_line = '"' + line.replace("\\", "\\\\").replace('"', '\\"') + '"'
            encoded_length = len(encoded_line)
            total_encoded += encoded_length

    return total_raw, total_encoded, total_encoded - total_raw


# Example usage
filename = "input.txt"
raw_length, encoded_length, difference = calculate_encoded_difference(filename)

print(f"Total raw length: {raw_length}")
print(f"Total encoded length: {encoded_length}")
print(f"Difference: {difference}")
