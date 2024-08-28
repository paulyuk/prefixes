# Prefixes Analyzer

## Summary
This is a tiny experiment that can take a large amount of 'big data' say from Kusto, identify prefixes and words using expressions, and then count unique ones in descending order, and show you the clusters.

The intent is to find patterns in things like resource names that you can focus on or filter away.

## Running

1) change file_path to the path of your CSV file (Excel can be used to by modifying the engine to be `openpyxl`)
2) install and run the python app

```bash
pip3 install -r requirements.txt
python3 prefix_small_words.py
```

3) examine the output of `prefix_counts_output.txt`
