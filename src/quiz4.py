from pathlib import Path

data_path = "./data"

csv_file = Path(data_path).glob("*.csv")
for file in csv_file:
  print(file)