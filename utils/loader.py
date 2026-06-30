import pandas as pd


class CSVLoader:

    def __init__(self):

        self.df = None

    def load_file(self, filepath):

        self.df = pd.read_csv(
            filepath,
            sep=None,
            engine="python"
        )

        self.df.columns = (
            self.df.columns
            .str.strip()
        )

        return self.df

    def get_file_numbers(self):

        return (
            self.df["File"]
            .astype(str)
            .unique()
            .tolist()
        )

    def get_current_columns(self):

        return [

            c

            for c in self.df.columns

            if "y" in c.lower()

        ]

    def get_curve(
            self,
            file_number,
            current_column
    ):

        row = self.df[
            self.df["File"]
            .astype(str)
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

        return (

            voltage[mask].reset_index(drop=True),

            current[mask].reset_index(drop=True)

        )
