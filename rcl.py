import re
from subprocess import call

call(["python", "cg_o.py"])

exit()
def Convert(string):
    li = list(string.split(","))
    return li

def fixer(test_lists_4, count1):
	t = test_lists_4
	return (t[count1], t[1+count1], t[2+count1], t[3+count1], t[4+count1], t[5+count1], t[6+count1], t[7+count1], t[8+count1], t[9+count1], t[10+count1], t[11+count1], t[12+count1], t[13+count1], t[14+count1], t[15+count1], t[16+count1], t[17+count1], t[18+count1], t[19+count1])
lines_s = []
lines_s2 = []
lines_s4 = []
lines_s_h = []
lines_s_h2 = []
lines_ss = []
count11 = 0
test_lists_2 = []
test_lists_5 = []

with open('r2.txt') as f:
	test_lists = f.readlines()

for a in test_lists:
	a = a.replace('[', '')
	a = a.replace(']', '')
	a = a.rstrip("\n")
	a = a.replace("(", '')
	a = a.replace(")", '')
	a = a.replace(" ", '')
	a = a.replace("-", '')
	test_lists_2.append(a)
test_lists_2 = list(dict.fromkeys(test_lists_2))
test_lists_3 = str(test_lists_2)
test_lists_3 = test_lists_3.replace('[', '')
test_lists_3 = test_lists_3.replace(']', '')
test_lists_3 = test_lists_3.replace("'", '')
test_lists_3 = test_lists_3.replace(" ", '')
test_lists_4 = Convert(test_lists_3)
print(test_lists_4)
tt = len(test_lists_4)
tt2 = int(tt) / 20
for a in range(0, int(tt2)):
	count1 = (int(a) * 19) + int(a)
	tt3 = fixer(test_lists_4, count1)
	test_lists_5.append(tt3)
test_lists_5 = list(dict.fromkeys(test_lists_5))
print(test_lists_5)
exit()
lines_s2 = test_lists_5
input_text2 = 'tractor'
if 'trai' in input_text2:
	input_text3 = 1
elif 'bus' in input_text2:
	input_text3 = 2
elif 'truc' in input_text2:
	input_text3 = 3
elif 'bicy' in input_text2:
	input_text3 = 4
elif 'airp' in input_text2:
	input_text3 = 5
elif 'boa' in input_text2:
	input_text3 = 6
elif 'motorc' in input_text2:
	input_text3 = 7
elif 'car' in input_text2:
	input_text3 = 8
elif 'tree' in input_text2:
	input_text3 = 9
elif 'fire' in input_text2:
	input_text3 = 10
elif 'crossw' in input_text2:
	input_text3 = 11
elif 'traffic li' in input_text2:
	input_text3 = 12
elif 'bridge' in input_text2:
	input_text3 = 13
elif 'tract' in input_text2:
	input_text3 = 14
elif 'taxi' in input_text2:
	input_text3 = 15
elif 'stair' in input_text2:
	input_text3 = 16
elif 'chim' in input_text2:
	input_text3 = 17
elif 'mountain' in input_text2:
	input_text3 = 18
elif 'parking' in input_text2:
	input_text3 = 19
with open('r1.txt') as f1:
	a1 = f1.readlines()
a2 = re.findall(input_text2, str(a1))
if len(a2) == 3:
	pass
elif len(a2) > 3:
	pass
elif len(a2) == 2:
	for b in a1:
		ati = b.translate({ord(i): None for i in 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz. '})
		if input_text2 in b:
			lines_s_h.append(ati)
	for b1 in lines_s2:
		if int(lines_s_h[0]) != int(b1[0]):
			lines_s.append(b1)
	for b1 in lines_s:
		if int(lines_s_h[1]) != int(b1[0]):
			lines_ss.append(b1)
	lines_ss = list(dict.fromkeys(lines_ss))
	lines_ss.append((9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
	lines_ss.append((9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
	lines_ss.append((9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
	lines_s3 = lines_ss
	try:
		if (lines_s3[0][input_text3] > lines_s3[1][input_text3]) and (lines_s3[0][input_text3] > lines_s3[2][input_text3]) and (lines_s3[0][input_text3] > lines_s3[3][input_text3]) and (lines_s3[0][input_text3] > lines_s3[4][input_text3]) and (lines_s3[0][input_text3] > lines_s3[5][input_text3]) and (lines_s3[0][input_text3] > lines_s3[6][input_text3]):
			print(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[1][input_text3] > lines_s3[0][input_text3]) and (lines_s3[1][input_text3] > lines_s3[2][input_text3]) and (lines_s3[1][input_text3] > lines_s3[3][input_text3]) and (lines_s3[1][input_text3] > lines_s3[4][input_text3]) and (lines_s3[1][input_text3] > lines_s3[5][input_text3]) and (lines_s3[1][input_text3] > lines_s3[6][input_text3]):
			print(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[2][input_text3] > lines_s3[0][input_text3]) and (lines_s3[2][input_text3] > lines_s3[1][input_text3]) and (lines_s3[2][input_text3] > lines_s3[3][input_text3]) and (lines_s3[2][input_text3] > lines_s3[4][input_text3]) and (lines_s3[2][input_text3] > lines_s3[5][input_text3]) and (lines_s3[2][input_text3] > lines_s3[6][input_text3]):
			print(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[3][input_text3] > lines_s3[0][input_text3]) and (lines_s3[3][input_text3] > lines_s3[1][input_text3]) and (lines_s3[3][input_text3] > lines_s3[2][input_text3]) and (lines_s3[3][input_text3] > lines_s3[4][input_text3]) and (lines_s3[3][input_text3] > lines_s3[5][input_text3]) and (lines_s3[3][input_text3] > lines_s3[6][input_text3]):
			print(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[4][input_text3] > lines_s3[0][input_text3]) and (lines_s3[4][input_text3] > lines_s3[1][input_text3]) and (lines_s3[4][input_text3] > lines_s3[2][input_text3]) and (lines_s3[4][input_text3] > lines_s3[3][input_text3]) and (lines_s3[4][input_text3] > lines_s3[5][input_text3]) and (lines_s3[4][input_text3] > lines_s3[6][input_text3]):
			print(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[5][input_text3] > lines_s3[0][input_text3]) and (lines_s3[5][input_text3] > lines_s3[1][input_text3]) and (lines_s3[5][input_text3] > lines_s3[2][input_text3]) and (lines_s3[5][input_text3] > lines_s3[3][input_text3]) and (lines_s3[5][input_text3] > lines_s3[4][input_text3]) and (lines_s3[5][input_text3] > lines_s3[6][input_text3]):
			print(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[6][input_text3] > lines_s3[0][input_text3]) and (lines_s3[6][input_text3] > lines_s3[1][input_text3]) and (lines_s3[6][input_text3] > lines_s3[2][input_text3]) and (lines_s3[6][input_text3] > lines_s3[3][input_text3]) and (lines_s3[6][input_text3] > lines_s3[4][input_text3]) and (lines_s3[6][input_text3] > lines_s3[5][input_text3]):
			print(str(lines_s3[6][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[6][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
	except IndexError:
		if (lines_s3[0][input_text3] > lines_s3[1][input_text3]) and (lines_s3[0][input_text3] > lines_s3[2][input_text3]) and (lines_s3[0][input_text3] > lines_s3[3][input_text3]) and (lines_s3[0][input_text3] > lines_s3[4][input_text3]) and (lines_s3[0][input_text3] > lines_s3[5][input_text3]):
			print(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[1][input_text3] > lines_s3[0][input_text3]) and (lines_s3[1][input_text3] > lines_s3[2][input_text3]) and (lines_s3[1][input_text3] > lines_s3[3][input_text3]) and (lines_s3[1][input_text3] > lines_s3[4][input_text3]) and (lines_s3[1][input_text3] > lines_s3[5][input_text3]):
			print(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[2][input_text3] > lines_s3[0][input_text3]) and (lines_s3[2][input_text3] > lines_s3[1][input_text3]) and (lines_s3[2][input_text3] > lines_s3[3][input_text3]) and (lines_s3[2][input_text3] > lines_s3[4][input_text3]) and (lines_s3[2][input_text3] > lines_s3[5][input_text3]):
			print(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[3][input_text3] > lines_s3[0][input_text3]) and (lines_s3[3][input_text3] > lines_s3[1][input_text3]) and (lines_s3[3][input_text3] > lines_s3[2][input_text3]) and (lines_s3[3][input_text3] > lines_s3[4][input_text3]) and (lines_s3[3][input_text3] > lines_s3[5][input_text3]):
			print(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[4][input_text3] > lines_s3[0][input_text3]) and (lines_s3[4][input_text3] > lines_s3[1][input_text3]) and (lines_s3[4][input_text3] > lines_s3[2][input_text3]) and (lines_s3[4][input_text3] > lines_s3[3][input_text3]) and (lines_s3[4][input_text3] > lines_s3[5][input_text3]):
			print(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
		if (lines_s3[5][input_text3] > lines_s3[0][input_text3]) and (lines_s3[5][input_text3] > lines_s3[1][input_text3]) and (lines_s3[5][input_text3] > lines_s3[2][input_text3]) and (lines_s3[5][input_text3] > lines_s3[3][input_text3]) and (lines_s3[5][input_text3] > lines_s3[4][input_text3]):
			print(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
			f = open("r1.txt", "a")
			f.write(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
			f.write("\n")
			f.close()
elif len(a2) == 1:
	for b in a1:
		ati = b.translate({ord(i): None for i in 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz. '})
		if input_text2 in b:
			lines_s_h.append(ati)
	for b1 in lines_s2:
		if int(lines_s_h[0]) != int(b1[0]):
			lines_s.append(b1)
	lines_s.append((9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
	lines_s.append((9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
	lines_s.append((9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
	lines_s3 = lines_s
	if (lines_s3[0][input_text3] > lines_s3[1][input_text3]) and (lines_s3[0][input_text3] > lines_s3[2][input_text3]) and (lines_s3[0][input_text3] > lines_s3[3][input_text3]) and (lines_s3[0][input_text3] > lines_s3[4][input_text3]) and (lines_s3[0][input_text3] > lines_s3[5][input_text3]) and (lines_s3[0][input_text3] > lines_s3[6][input_text3]) and (lines_s3[0][input_text3] > lines_s3[7][input_text3]):
		print(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[0][0])
	if (lines_s3[1][input_text3] > lines_s3[0][input_text3]) and (lines_s3[1][input_text3] > lines_s3[2][input_text3]) and (lines_s3[1][input_text3] > lines_s3[3][input_text3]) and (lines_s3[1][input_text3] > lines_s3[4][input_text3]) and (lines_s3[1][input_text3] > lines_s3[5][input_text3]) and (lines_s3[1][input_text3] > lines_s3[6][input_text3]) and (lines_s3[1][input_text3] > lines_s3[7][input_text3]):
		print(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[1][0])
	if (lines_s3[2][input_text3] > lines_s3[0][input_text3]) and (lines_s3[2][input_text3] > lines_s3[1][input_text3]) and (lines_s3[2][input_text3] > lines_s3[3][input_text3]) and (lines_s3[2][input_text3] > lines_s3[4][input_text3]) and (lines_s3[2][input_text3] > lines_s3[5][input_text3]) and (lines_s3[2][input_text3] > lines_s3[6][input_text3]) and (lines_s3[2][input_text3] > lines_s3[7][input_text3]):
		print(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[2][0])
	if (lines_s3[3][input_text3] > lines_s3[0][input_text3]) and (lines_s3[3][input_text3] > lines_s3[1][input_text3]) and (lines_s3[3][input_text3] > lines_s3[2][input_text3]) and (lines_s3[3][input_text3] > lines_s3[4][input_text3]) and (lines_s3[3][input_text3] > lines_s3[5][input_text3]) and (lines_s3[3][input_text3] > lines_s3[6][input_text3]) and (lines_s3[3][input_text3] > lines_s3[7][input_text3]):
		print(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[3][0])
	if (lines_s3[4][input_text3] > lines_s3[0][input_text3]) and (lines_s3[4][input_text3] > lines_s3[1][input_text3]) and (lines_s3[4][input_text3] > lines_s3[2][input_text3]) and (lines_s3[4][input_text3] > lines_s3[3][input_text3]) and (lines_s3[4][input_text3] > lines_s3[5][input_text3]) and (lines_s3[4][input_text3] > lines_s3[6][input_text3]) and (lines_s3[4][input_text3] > lines_s3[7][input_text3]):
		print(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[4][0])
	if (lines_s3[5][input_text3] > lines_s3[0][input_text3]) and (lines_s3[5][input_text3] > lines_s3[1][input_text3]) and (lines_s3[5][input_text3] > lines_s3[2][input_text3]) and (lines_s3[5][input_text3] > lines_s3[3][input_text3]) and (lines_s3[5][input_text3] > lines_s3[4][input_text3]) and (lines_s3[5][input_text3] > lines_s3[6][input_text3]) and (lines_s3[5][input_text3] > lines_s3[7][input_text3]):
		print(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[5][0])
	if (lines_s3[6][input_text3] > lines_s3[0][input_text3]) and (lines_s3[6][input_text3] > lines_s3[1][input_text3]) and (lines_s3[6][input_text3] > lines_s3[2][input_text3]) and (lines_s3[6][input_text3] > lines_s3[3][input_text3]) and (lines_s3[6][input_text3] > lines_s3[4][input_text3]) and (lines_s3[6][input_text3] > lines_s3[5][input_text3]) and (lines_s3[6][input_text3] > lines_s3[7][input_text3]):
		print(str(lines_s3[6][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[6][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[6][0])
	if (lines_s3[7][input_text3] > lines_s3[0][input_text3]) and (lines_s3[7][input_text3] > lines_s3[1][input_text3]) and (lines_s3[7][input_text3] > lines_s3[2][input_text3]) and (lines_s3[7][input_text3] > lines_s3[3][input_text3]) and (lines_s3[7][input_text3] > lines_s3[4][input_text3]) and (lines_s3[7][input_text3] > lines_s3[5][input_text3]) and (lines_s3[7][input_text3] > lines_s3[6][input_text3]):
		print(str(lines_s3[7][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[7][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
		lines_s_h2.append(lines_s3[7][0])
	for b1 in lines_s3:
		if int(lines_s_h2[0]) != int(b1[0]):
			lines_s4.append(b1)
	lines_s3 = lines_s4
	if (lines_s3[0][input_text3] > lines_s3[1][input_text3]) and (lines_s3[0][input_text3] > lines_s3[2][input_text3]) and (lines_s3[0][input_text3] > lines_s3[3][input_text3]) and (lines_s3[0][input_text3] > lines_s3[4][input_text3]) and (lines_s3[0][input_text3] > lines_s3[5][input_text3]) and (lines_s3[0][input_text3] > lines_s3[6][input_text3]):
		print(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[0][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
	if (lines_s3[1][input_text3] > lines_s3[0][input_text3]) and (lines_s3[1][input_text3] > lines_s3[2][input_text3]) and (lines_s3[1][input_text3] > lines_s3[3][input_text3]) and (lines_s3[1][input_text3] > lines_s3[4][input_text3]) and (lines_s3[1][input_text3] > lines_s3[5][input_text3]) and (lines_s3[1][input_text3] > lines_s3[6][input_text3]):
		print(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[1][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
	if (lines_s3[2][input_text3] > lines_s3[0][input_text3]) and (lines_s3[2][input_text3] > lines_s3[1][input_text3]) and (lines_s3[2][input_text3] > lines_s3[3][input_text3]) and (lines_s3[2][input_text3] > lines_s3[4][input_text3]) and (lines_s3[2][input_text3] > lines_s3[5][input_text3]) and (lines_s3[2][input_text3] > lines_s3[6][input_text3]):
		print(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[2][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
	if (lines_s3[3][input_text3] > lines_s3[0][input_text3]) and (lines_s3[3][input_text3] > lines_s3[1][input_text3]) and (lines_s3[3][input_text3] > lines_s3[2][input_text3]) and (lines_s3[3][input_text3] > lines_s3[4][input_text3]) and (lines_s3[3][input_text3] > lines_s3[5][input_text3]) and (lines_s3[3][input_text3] > lines_s3[6][input_text3]):
		print(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[3][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
	if (lines_s3[4][input_text3] > lines_s3[0][input_text3]) and (lines_s3[4][input_text3] > lines_s3[1][input_text3]) and (lines_s3[4][input_text3] > lines_s3[2][input_text3]) and (lines_s3[4][input_text3] > lines_s3[3][input_text3]) and (lines_s3[4][input_text3] > lines_s3[5][input_text3]) and (lines_s3[4][input_text3] > lines_s3[6][input_text3]):
		print(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[4][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
	if (lines_s3[5][input_text3] > lines_s3[0][input_text3]) and (lines_s3[5][input_text3] > lines_s3[1][input_text3]) and (lines_s3[5][input_text3] > lines_s3[2][input_text3]) and (lines_s3[5][input_text3] > lines_s3[3][input_text3]) and (lines_s3[5][input_text3] > lines_s3[4][input_text3]) and (lines_s3[5][input_text3] > lines_s3[6][input_text3]):
		print(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[5][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
	if (lines_s3[6][input_text3] > lines_s3[0][input_text3]) and (lines_s3[6][input_text3] > lines_s3[1][input_text3]) and (lines_s3[6][input_text3] > lines_s3[2][input_text3]) and (lines_s3[6][input_text3] > lines_s3[3][input_text3]) and (lines_s3[6][input_text3] > lines_s3[4][input_text3]) and (lines_s3[6][input_text3] > lines_s3[5][input_text3]):
		print(str(lines_s3[6][0]) + ' This is definitely a ' + str(input_text2))
		f = open("r1.txt", "a")
		f.write(str(lines_s3[6][0]) + ' This is definitely a ' + str(input_text2))
		f.write("\n")
		f.close()
