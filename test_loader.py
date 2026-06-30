from utils.loader import CSVLoader

loader = CSVLoader()

loader.load_file("data/raw/All_Data (1).csv")

print(loader.get_file_numbers())

print(loader.get_current_columns())

voltage, current = loader.get_curve(
    loader.get_file_numbers()[0],
    loader.get_current_columns()[0]
)

print(voltage.head())

print(current.head())
