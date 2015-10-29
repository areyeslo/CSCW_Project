import csv
with open('output.csv', 'w', newline='') as fp:
	a = csv.writer(fp, delimiter=',')
	
	a.writerows(data)