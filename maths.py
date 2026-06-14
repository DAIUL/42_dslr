import math
import pandas as pd
import sys


def clean_values(values: tuple) -> tuple:
	clean_values = [x for x in values if not pd.isna(x)]
	return clean_values

def ft_count(values: tuple) -> float:
	values = clean_values(values)

	i = 0
	for value in values:
		i += 1
		
	return i


def ft_mean(values: tuple) -> float:
	values = clean_values(values)

	mean_value = sum(values) / len(values)
	return mean_value


def ft_min(values: tuple) -> float:
	values = clean_values(values)

	min = sorted(values)[0]
	return min


def ft_max(values: tuple) -> float:
	values = clean_values(values)

	max = sorted(values)[len(values) - 1]
	return max


def ft_median(values: tuple) -> float:
	values = clean_values(values)

	values = sorted(values)
	if len(values) % 2 == 0:
		median_mid = (values[(len(values) // 2) - 1], values[len(values) // 2])
		median_value = sum(median_mid) / 2
	else:
		median_value = values[len(values) // 2]
	return median_value


def ft_quartile(values: tuple) -> list:
	values = clean_values(values)

	values = sorted(values)
	mid = len(values) // 2

	if len(values) % 2 == 0:
		lower_values = values[:mid]
		upper_values = values[mid:]
	else:
		lower_values = values[:mid+1]
		upper_values = values[mid:]

	q1_value = ft_median(lower_values)
	q3_value = ft_median(upper_values)
	return [q1_value, q3_value]


def ft_var(values: tuple) -> float:
	values = clean_values(values)

	mean = ft_mean(values)
	var = sum([(x - mean)**2 for x in values]) / len(values)
	return var


def ft_std(values: tuple) -> float:
	values = clean_values(values)

	std = math.sqrt(ft_var(values))
	return std

def ft_eta_squared(groups: dict) -> float:

	all_values = []
	for values in groups.values():
		all_values.extend(values)
	
	total_mean = ft_mean(all_values)

	ss_total = 0
	ss_between = 0

	for values in groups.values():

		ss_total += sum((x - total_mean) ** 2 for x in values)

		house_mean = ft_mean(values)
		ss_between += ft_count(values) * (house_mean - total_mean) ** 2

	return ss_between / ss_total