import pandas as pd
import argparse
import json

VERSION = "2.1.0"

def analyze(input_file, output_file):
    df = pd.read_csv(input_file)
    numeric_cols = df.select_dtypes(include='number').columns
    result = {
        "version": VERSION,
        "row_count": len(df),
        "columns": list(df.columns),
        "mean_values": df.mean(numeric_only=True).to_dict(),
        "median_values": df.median(numeric_only=True).to_dict(),
        "max_values": df.max(numeric_only=True).to_dict(),
        "min_values": df.min(numeric_only=True).to_dict(),
        "sum_values": df[numeric_cols].sum().to_dict()
    }
    with open(output_file, "w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    analyze(args.input, args.output)
