import re
import pandas as pd
from collections import Counter, defaultdict

def get_prefix_counts_with_items(data):
    def split_words(item):
        # Find sequences of capitalized words and other patterns
        words = re.findall(r'[A-Z][a-z]*|[a-z]+|[A-Z]+(?=[A-Z]|$)', item)
        # Split by hyphens and flatten the list
        flattened_words = [word for part in words for word in part.split('-')]
        return flattened_words

    # Find prefixes for each item in data
    prefixes = [split_words(item) for item in data]

    # Flatten the list of lists into a single list of words
    flattened_prefixes = [word for sublist in prefixes for word in sublist]

    # Filter out single character prefixes
    filtered_prefixes = [word for word in flattened_prefixes if len(word) > 1]

    # Count the frequency of each prefix
    prefix_counts = Counter(filtered_prefixes)

    # Map each prefix to the list of items from the original data that contain that prefix
    prefix_to_items = defaultdict(list)
    for item in data:
        item_prefixes = split_words(item)
        for prefix in item_prefixes:
            if len(prefix) > 1:
                prefix_to_items[prefix].append(item)

    return prefix_counts, prefix_to_items

# Example usage
data = [
    "PrefixToFind1",
    "PrefixToFind2",
    "PrefixToFind3",
    "Other-Prefix-1",
    "Other-Prefix-2",
    "Outlier"
]

# Load data from spreadsheet
file_path = '/Users/paulyuk/data/networkquery.csv'  # Update this with the path to your spreadsheet
sheet_name = 'appswithip'  # Update this with the name of your sheet if necessary

# Read the spreadsheet into a DataFrame
df = pd.read_csv(file_path)

# Assuming the data is in the first column
data = df.iloc[:, 3].tolist()

prefix_counts, prefix_to_items = get_prefix_counts_with_items(data)

# Print and write the counts of each prefix, sorted by count descending
output_file_path = 'prefix_counts_output.txt'  # Update this with the desired output file path

with open(output_file_path, 'w') as file:
    file.write("Prefix Counts (sorted by count descending):\n")
    print("Prefix Counts (sorted by count descending):")
    for prefix, count in sorted(prefix_counts.items(), key=lambda item: item[1], reverse=True):
        line = f"{prefix}: {count}\n"
        print(line, end='')
        file.write(line)

    file.write("\nPrefixes with Counts and Items:\n")
    print("\nPrefixes with Counts and Items:")
    for prefix, items in sorted(prefix_to_items.items(), key=lambda item: prefix_counts[item[0]], reverse=True):
        line = f"{prefix} ({prefix_counts[prefix]}): {items}\n"
        print(line, end='')
        file.write(line)
