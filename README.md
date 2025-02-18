# CSV Transformer for EverBank to Simplifi

A command-line tool to transform EverBank CSV export files into a format compatible with Simplifi.

## Features

- Filters transactions from a specified date
- Combines credit and debit columns into a single amount column
- Renames columns to match Simplifi's format
- Removes currency symbols and extra spaces from amounts
- Preserves transaction dates and descriptions

## Installation

This project uses Python. Make sure you have Python installed on your system.

## Usage

```bash
python transform_csv.py INPUT_FILE OUTPUT_FILE --date YYYY-MM-DD
```

### Arguments

- `INPUT_FILE`: Path to the EverBank CSV export file
- `OUTPUT_FILE`: Path where the transformed CSV should be saved
- `--date` or `-d`: Filter transactions from this date (format: YYYY-MM-DD)

### Example

```bash
python transform_csv.py examples/input.csv examples/output.csv --date 2024-01-01
```

### Input CSV Format

The tool expects an EverBank CSV file with the following columns:

- Date (MM/DD/YYYY format)
- Description
- Credits(+)
- Debits(-)

### Output CSV Format

The transformed CSV will have these columns:

- Date
- Payee (from Description)
- Amount (combined from Credits/Debits)

## Error Handling

The tool includes error handling for:

- Invalid input file paths
- Invalid date formats
- General processing errors

## License

See LICENSE file for details.
