import matplotlib.pyplot as plt
import pandas as pd
import sys
import argparse
from utils import csv_check, column_check

# Which Hogwarts course has a homogeneous score distribution between all four houses?


def parse_args():
	
	parser = argparse.ArgumentParser(
		description='Display course score distribution between houses'
	)
	parser.add_argument('dataset')
	parser.add_argument('course')
	
	return parser.parse_args()


def course_values_per_house(data: pd.DataFrame, course: str) -> dict:

	houses = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']

	return {
		house: data.loc[data['Hogwarts House'] == house, course].dropna() 
		for house in houses
	}


def display_histogram(groups: dict, course: str) -> None:

	for house, values in groups.items():
		plt.hist(values, alpha=0.3, label=house)

	plt.legend()
	plt.title(course)
	plt.show()


def main():

	args = parse_args()

	try:		

		path = csv_check(args.dataset)
		data = pd.read_csv(path)
		numeric_data = data.select_dtypes(include='number')

		course = column_check(numeric_data, args.course)
		
		groups = course_values_per_house(data, course)
			
		display_histogram(groups, course)

	except Exception as e:
		print(f"Error : {e}")


if __name__ == '__main__':
	main()