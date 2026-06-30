import pandas as pd


class CSVLoader:
    """
    Loads the experimental CSV and returns
    voltage/current data for a selected File.
    """

    def __init__(self):
        self.df = None

    def load_file(self, filepath):
        """Load CSV file."""

        self.df = pd.read_csv(
            filepath,
            sep=None,
            engine="python"
        )

        # Remove extra spaces from column names
        self.df.columns = self.df.columns.str.strip()

        if "File" not in self.df.columns:
            raise ValueError("'File' column not found.")

        return self.df

    def get_file_numbers(self):
        """Return all unique file numbers."""

        return (
            self.df["File"]
            .astype(str)
            .unique()
            .tolist()
        )

    def get_current_columns(self):
        """Return all current columns."""

        current_columns = []

        for col in self.df.columns:

            if "y" in col.lower():

                current_columns.append(col)

        return current_columns

    def get_curve(self, file_number, current_column):
        """
        Returns voltage and current arrays
        for one experiment.
        """

        row = self.df[
            self.df["File"].astype(str)
            ==
            str(file_number)
        ]

        voltage = pd.to_numeric(
            row["1x V"],
            errors="coerce"
        )

        current = pd.to_numeric(
            row[current_column],
            errors="coerce"
        )

        mask = (
            voltage.notna()
            &
            current.notna()
        )

        voltage = voltage[mask].reset_index(drop=True)
        current = current[mask].reset_index(drop=True)

        return voltage, current
