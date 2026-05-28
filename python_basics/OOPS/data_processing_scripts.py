import pandas as pd

def main():
    # Step 1: Load data
    data = pd.read_csv("data.csv")   # Replace with your file name
    print("Original Data:")
    print(data.head())

    # Step 2: Handle missing values (fill with 0)
    data = data.fillna(0)

    # Step 3: Basic processing - calculate average of a column
    if "value" in data.columns:
        avg = data["value"].mean()
        print(f"\nAverage of 'value' column: {avg}")

    # Step 4: Add a new column (e.g., double the values)
    if "value" in data.columns:
        data["double_value"] = data["value"] * 2

    # Step 5: Save processed data
    data.to_csv("processed_data.csv", index=False)
    print("\nProcessed data saved to 'processed_data.csv'.")

if __name__ == "__main__":
    main()
