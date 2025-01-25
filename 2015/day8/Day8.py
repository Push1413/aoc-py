import re

def calculate_difference(filename):
    total_raw = 0
    total_decoded = 0

    with open(filename, "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            # Raw length: the string itself with quotes and escape sequences
            raw_length = len(line)
            total_raw += raw_length

            # Decoded length: after removing quotes and interpreting escape sequences
            decoded_line = bytes(line, "utf-8").decode('unicode_escape')
            decoded_length = len(decoded_line) - 2  # Subtract 2 for the quotes
            total_decoded += decoded_length

    return total_raw, total_decoded, total_raw - total_decoded


# Example usage
filename = "input.txt"
raw_length, decoded_length, difference = calculate_difference(filename)

print(f"Total raw length: {raw_length}")
print(f"Total decoded length: {decoded_length}")
print(f"Difference: {difference}")
