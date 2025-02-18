import csv
from datetime import datetime
import pytest
from transform_csv import transform_csv


@pytest.fixture
def input_csv():
    return "examples/input.csv"


@pytest.fixture
def output_csv():
    return "examples/output.csv"


@pytest.fixture
def expected_output():
    results = []
    with open("examples/output.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Only include records from 2025-02-12 onwards
            date = datetime.strptime(row["Date"], "%m/%d/%Y")
            if date >= datetime.strptime("2025-02-12", "%Y-%m-%d"):
                results.append(row)
    return results


def test_transform_csv(input_csv, expected_output, tmp_path):
    # Create a temporary output file
    temp_output = tmp_path / "test_output.csv"

    # Run the transformation
    transform_csv(input_csv, str(temp_output), "2025-02-12")

    # Read the generated output
    actual_output = []
    with open(temp_output, "r") as f:
        reader = csv.DictReader(f)
        actual_output = list(reader)

    # Compare the results
    assert len(actual_output) == len(expected_output)

    for actual, expected in zip(actual_output, expected_output):
        assert actual["Date"] == expected["Date"]
        assert actual["Payee"] == expected["Payee"]
        assert actual["Amount"] == expected["Amount"]
