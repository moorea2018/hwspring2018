
import csv
with open('roster.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        gradyear = []
        gpa = []
        for grad in readcsv:
                if grads == "2018" and grades > "2.0":
                        gradyear.append(grads)
                        gpa.append(grades)
        print gradyear
        print gpa
import csv
with open('roster.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')
	gradyear = []
	gpa = []
	for grad in readcsv:
		if grads == "2018" and grades > "2.0":
			gradyear.append(grads)
			gpa.append(grades)
	print gradyear
	print gpa
