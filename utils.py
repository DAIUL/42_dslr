import pandas as pd
import os


def csv_check(path: str) -> str:

	if not os.path.isfile(path):
		raise FileNotFoundError(
			f"{path} not found"
		)
	
	if not path.endswith('.csv'):
		raise ValueError(
			f"{path} is not a csv file"
		)
	
	return path

def column_check(data: pd.DataFrame, column: str) -> str:

	if column not in data.columns:
		raise ValueError(
			f"{column} is not a valid course\n"
			f"Available : {list(data.columns)}"
		)
	
	return column