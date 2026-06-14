import matplotlib.pyplot as plt
import pandas as pd
import sys
import argparse
from utils import csv_check, column_check
from maths import ft_eta_squared, ft_min

# Which Hogwarts course has a homogeneous score distribution between all four houses?

	# On cherche a savoir quel dispertion est la plus homogene.
	# Soit : Quelle proportion de la variance totale est expliquée par les groupes ?
	# Pour ca on va chercher le cours ou l'appartenance a une certaine maison ne permet pas,
	# ou le moins possible, de determiner ou predire la note d'un eleve.
	# Moins l'info m'est utile, plus les histogramme de chaque classe se supperposent.
	
	# Pour ca on calcule la moyenne globale de toutes les notes, peu importe la classe.
	# Puis on calucle la variance globale. Cela nous donne la dispertion globale des notes.
	# Ensuite on va calculer la variance expliquee par chaque maison,
	# donc : sum( [nb d'eleves dans la maison] * (moyenne de la classe - moyenne globale)**2 )

	# Ca nous laisse avec la variance totale et la variance inter-maison (somme de la variance des groupes)

	# On calcule 'eta squared' qui correspond a notre question initiale
	# donc : variance des groupes / variance totale 

	# Plus on est proche de 1 plus la maison explique la note,
	# plus on est proche de 0 moins la maison permet de determiner la note

	# Pour repondre a la question on cherche le cours qui a le resultat le plus proche de 0



def parse_args():
	
	parser = argparse.ArgumentParser(
		description='Display course score distribution between houses'
	)
	parser.add_argument('dataset')
	
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


def get_most_homogenous(data: pd.DataFrame) -> str:

	numeric_data = data.select_dtypes(include='number')
	eta_squared = {}

	for course in numeric_data.columns:
			
		groups = course_values_per_house(data, course)

		eta_squared[course] = ft_eta_squared(groups)

	most_homogenous = None
	smallest_eta = float('inf')
		
	for key, value in eta_squared.items():
		if value < smallest_eta:
			smallest_eta = value
			most_homogenous = key

	return most_homogenous


def main():

	args = parse_args()

	try:		

		path = csv_check(args.dataset)
		data = pd.read_csv(path)
		most_homogenous = get_most_homogenous(data)

		display_histogram(course_values_per_house(data, most_homogenous), most_homogenous)

	except Exception as e:
		print(f"Error : {e}")


if __name__ == '__main__':
	main()