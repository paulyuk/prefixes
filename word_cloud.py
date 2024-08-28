import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def read_prefix_counts(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    prefix_counts = {}
    for line in lines:
        line = line.strip()
        if line:
            match = re.match(r'^(.*): (\d+)$', line)
            if match:
                prefix = match.group(1)
                count = int(match.group(2))
                prefix_counts[prefix] = count

    return prefix_counts

def generate_word_cloud(prefix_counts, output_image_path):
    # Get the top 50 prefixes
    top_prefixes = dict(Counter(prefix_counts).most_common(50))

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(top_prefixes)

    # Display the word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(output_image_path)
    plt.show()

# Path to the prefix counts file
file_path = 'prefix_counts_output.txt'
# Path to save the word cloud image
output_image_path = 'prefix_word_cloud.png'

# Read the prefix counts from the file
prefix_counts = read_prefix_counts(file_path)

# Generate and save the word cloud
generate_word_cloud(prefix_counts, output_image_path)
