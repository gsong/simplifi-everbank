import csv
from datetime import datetime


def transform_csv(input_file: str, output_file: str, date: str) -> None:
    """
    Transform a CSV file by filtering dates and restructuring columns.

    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to output CSV file
        date (str): Date string in YYYY-MM-DD format to filter from
    """
    # Convert filter date to datetime object
    filter_date = datetime.strptime(date, "%Y-%m-%d")

    # Read input CSV
    def read_input_csv():
        with open(input_file, "r") as f:
            reader = csv.DictReader(f)
            return list(reader)

    # Filter rows by date
    def filter_by_date(rows):
        filtered_rows = []
        for row in rows:
            row_date = datetime.strptime(row["Date"], "%m/%d/%Y")
            if row_date >= filter_date:
                filtered_rows.append(row)
        return filtered_rows

    # Transform row data (combine amounts, rename columns)
    def transform_row(row):
        amount = row.get("Credits(+)") or row.get("Debits(-)")
        # Remove any extra spaces, $ symbols, and ensure single $ is removed
        amount = amount.replace(" ", "").replace("$", "")
        
        return {
            "Date": row["Date"],
            "Payee": row["Description"],
            "Amount": amount
        }

    # Write output CSV
    def write_output_csv(transformed_data):
        fieldnames = ["Date", "Payee", "Amount"]
        with open(output_file, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transformed_data)

    # Main transformation logic
    input_data = read_input_csv()
    filtered_data = filter_by_date(input_data)
    transformed_data = [transform_row(row) for row in filtered_data]
    write_output_csv(transformed_data)


def main():
    print("Hello from simplifi-everbank!")


if __name__ == "__main__":
    main()
