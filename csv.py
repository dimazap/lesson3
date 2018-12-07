import csv
csv = 'input'
csvout = csv.writer(jobs)

with open('jobs.csv', 'w', encoding='utf-8', newline='') as f:
	fields = ['name', 'age', 'job']
	writer = csvout.DictWriter(f, fields, delimiter=';')
	writer.writeheader()
	content = [
		{'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
		{'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
		{'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
	]
	for key, value in content.items():
		writer.writerow([key, value])