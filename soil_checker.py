import csv

def check(soil):
	a = int(soil[0])
	b = int(soil[1])
	c = int(soil[2])
	d = int(soil[3])

	if 0 <= a <= 5 and 0 <= b <= 20 and 0 <= c <= 50 and 75 <= d <= 100:
		print "Coarse sand"
	elif 0 <= a <= 5 and 0 <= b <= 20 and 50 <= c <= 100 and 75 <= d <= 100:
		print "Fine sand"
	elif 5 <= a <= 10 and 0 <= b <= 25 and 0 <= c <= 40 and 65 <= d <= 95:
		print "Coarse clayey sand"
	elif 5 <= a <= 10 and 0 <= b <= 25 and 40 <= c <= 95 and 65 <= d <= 95:
		print "Fine clayey sand"
	elif 10 <= a <= 15 and 0 <= b <= 30 and 0 <= c <= 40 and 55 <= d <= 90:
		print "Coarse sandy clay"
	elif 10 <= a <= 15 and 0 <= b <= 30 and 40 <= c <= 90 and 55 <= d <= 90:
		print "Fine sandy clay"
	else:
		print "oops"

f = open('SoilData.csv')
csv_f = csv.reader(f)

for row in csv_f:
	soil = []
	check(soil.extend(row))

print soilA


f.close()
