import math
import argparse
import sys
import pandas as pd
from maths import ft_quartile, ft_min, ft_count, ft_max, ft_mean, ft_median, ft_std, ft_var
from utils import csv_check


def parse_args():

	parser = argparse.ArgumentParser(
		description='Describe mathematical values of a dataset (same as .describe())'
	)
	parser.add_argument('dataset')

	return parser.parse_args()


def get_stats_dataset(numeric_data: pd.DataFrame) -> pd.DataFrame:

	stats = pd.DataFrame()

	for column in numeric_data.columns:

		values = numeric_data[column]
		quartile = ft_quartile(values)

		stats[column] = [
			ft_count(values),
			ft_mean(values),
			ft_std(values),
			ft_min(values),
			quartile[0],
			ft_median(values),
			quartile[1],
			ft_max(values)
		]

	stats.index = [
		'Count',
		'Mean',
		'Std',
		'Min',
		'25%',
		'50%',
		'75%',
		'Max'
	]

	return stats


def main() -> None:

	args = parse_args()
	
	path = csv_check(args.dataset)
	data = pd.read_csv(path)
	numeric_data = data.select_dtypes(include="number")

	stats = get_stats_dataset(numeric_data)

	print(stats)
	
	return None


if __name__ == '__main__':
	main()