import csv

def check(ele1,ele2,ele3,ele4):
	a = int(ele1)
	b = int(ele2)
	c = int(ele3)
	d = int(ele4)

	if 0 <= a <= 5 and 0 <= b <= 20 and 0 <= c <= 50 and 75 <= d <= 100:
		return "Coarse sand"
	elif 0 <= a <= 5 and 0 <= b <= 20 and 50 <= c <= 100 and 75 <= d <= 100:
		return "Fine sand"
	elif 5 <= a <= 10 and 0 <= b <= 25 and 0 <= c <= 40 and 65 <= d <= 95:
		return "Coarse clayey sand"
	elif 5 <= a <= 10 and 0 <= b <= 25 and 40 <= c <= 95 and 65 <= d <= 95:
		return "Fine clayey sand"
	elif 10 <= a <= 15 and 0 <= b <= 30 and 0 <= c <= 40 and 55 <= d <= 90:
		return "Coarse sandy clay"
	elif 10 <= a <= 15 and 0 <= b <= 30 and 40 <= c <= 90 and 55 <= d <= 90:
		return "Fine sandy clay"
	elif 15 <= a <= 25 and 0 <= b <= 35 and 40 <= d <= 85:
		return "Clay"
	elif 0 <= a <= 50 and 20 <= b <= 100 and 0 <= d <= 80:
		return "Silt"
	else:
		return "Something Else"

f = open('SoilData.csv')
csv_f = csv.reader(f)

i = 1
for row in csv_f:
	soil = []
	soil.extend(row)
	check(*soil)
	print str(i) + " is: " + check(*soil)
	i+=1

f.close()
