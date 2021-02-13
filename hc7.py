from pynput.mouse import Button, Controller
import time
import json
def hc_solver1(a, dd2):
	if dd2 and '0' in a:
		if dd2 in a:
			mouse.position = (490, 285)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '1' in a:
		if dd2 in a:
			mouse.position = (634, 282)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '2' in a:
		if dd2 in a:
			mouse.position = (753, 296)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '3' in a:
		if dd2 in a:
			mouse.position = (492, 420)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '4' in a:
		if dd2 in a:
			mouse.position = (633, 422)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '5' in a:
		if dd2 in a:
			mouse.position = (750, 422)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '6' in a:
		if dd2 in a:
			mouse.position = (503, 548)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '7' in a:
		if dd2 in a:
			mouse.position = (624, 540)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '8' in a:
		if dd2 in a:
			mouse.position = (754, 535)
			mouse.click(Button.left, 1)
			time.sleep(1)

def hc_solver2(a, dd2):
	if dd2 and '9' in a:
		if dd2 in a:
			mouse.position = (490, 285)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '10' in a:
		if dd2 in a:
			mouse.position = (634, 282)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '11' in a:
		if dd2 in a:
			mouse.position = (753, 296)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '12' in a:
		if dd2 in a:
			mouse.position = (492, 420)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '13' in a:
		if dd2 in a:
			mouse.position = (633, 422)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '14' in a:
		if dd2 in a:
			mouse.position = (750, 422)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '15' in a:
		if dd2 in a:
			mouse.position = (503, 548)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '16' in a:
		if dd2 in a:
			mouse.position = (624, 540)
			mouse.click(Button.left, 1)
			time.sleep(1)
	elif dd2 and '17' in a:
		if dd2 in a:
			mouse.position = (754, 535)
			mouse.click(Button.left, 1)
			time.sleep(1)
mouse = Controller()
with open('hc.txt') as f11:
	data = json.loads(f11.read())
	dd = data['requester_question']['en']
	dd3 = data["tasklist"]
	count1 = len(dd3)
	if 'motorbus' not in dd:
		dd2 = dd.replace('Please click each image containing a ','')
		print(dd2)
	else:
		dd2 = 'bus'
		print(dd2)
if count1 < 10:
	for b in range(1, 3):
		with open('h' + str(b) + '.txt') as f1:
			a1 = f1.readlines()
			for a in a1:
				hc_solver1(a, dd2)
	mouse.position = (1321, 340)
	mouse.click(Button.left, 1)
	time.sleep(1)
if count1 > 10:
	time.sleep(1)
	for b in range(1, 3):
		with open('h' + str(b) + '.txt') as f1:
			a1 = f1.readlines()
			for a in a1:
				hc_solver2(a, dd2)
	mouse.position = (1321, 340)
	mouse.click(Button.left, 1)
	time.sleep(1)
	for b in range(3, 5):
		with open('h' + str(b) + '.txt') as f1:
			a1 = f1.readlines()
			for a in a1:
				hc_solver2(a, dd2)
	mouse.position = (1321, 340)
	mouse.click(Button.left, 1)
else:
	exit()
