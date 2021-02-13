import json
import requests
import re
def hc_solver(filePath, count):
	try:
		proxies = {'http':  'socks5://127.0.0.1:9050',
		                       'https': 'socks5://127.0.0.1:9050'}
		searchUrl = 'https://yandex.ru/images/search'
		files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
		params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
		response = requests.post(searchUrl, params=params, files=files, proxies=proxies)
		query_string = json.loads(response.content)['blocks'][0]['params']['url']
		img_search_url= searchUrl + '?' + query_string
		a = requests.get(img_search_url, proxies=proxies)
		b = a.text
		t1 = re.findall(r'train', b)
		t2 = re.findall(r'Train', b)
		t22 = re.findall(r'TRAIN', b)
		t23 = re.findall(r'поезд', b)
		t24 = re.findall(r'трамва', b)
		t3 = len(t1) + len(t2) + len(t22) + len(t23) + len(t24)
		b1 = re.findall(r'bus', b)
		b2 = re.findall(r'Bus', b)
		b22 = re.findall(r'BUS', b)
		b111 = re.findall(r'motorbus', b)
		b112 = re.findall(r'Motorbus', b)
		b113 = re.findall(r'MOTORBUS', b)
		b114 = re.findall(r'автобус', b)
		b3 = len(b1) + len(b2) + len(b22) + len(b111) + len(b112) + len(b113) + len(b114)
		b4 = re.findall(r'abuse', b)
		b5 = re.findall(r'aria-busy', b)
		b222 = re.findall(r'business', b)
		b223 = re.findall(r'Business', b)
		b224 = re.findall(r'BUSINESS', b)
		b225 = re.findall(r'airbus', b)
		b226 = re.findall(r'Airbus', b)
		b227 = re.findall(r'AIRBUS', b)
		b228 = re.findall(r'Busdriver', b)
		b229 = re.findall(r'Bus driver', b)
		b230 = re.findall(r'Bus Driver', b)
		b55 = len(b4) + len(b5) + len(b222) + len(b223) + len(b224) + len(b225) + len(b226) + len(b227) + len(b228) + len(b229) + len(b230)
		b6 = int(b3) - int(b55)
		tr1 = re.findall(r'truck', b)
		tr2 = re.findall(r'Truck', b)
		tr3 = re.findall(r'TRUCK', b)
		tr31 = re.findall(r'грузовик', b)
		tr32 = re.findall(r'пожарной', b)
		tr33 = re.findall(r'Огонь', b)
		tr4 = len(tr1) + len(tr2) + len(tr3) + len(tr31) + len(tr32) + len(tr33)
		by1 = re.findall(r'bicycle', b)
		by2 = re.findall(r'Bicycle', b)
		by3 = re.findall(r'BICYCLE', b)
		by31 = re.findall(r'велосипед', b)
		by4 = len(by1) + len(by2) + len(by3) + len(by31)
		a1 = re.findall(r'airplane', b)
		a2 = re.findall(r'Airplane', b)
		a3 = re.findall(r'AIRPLANE', b)
		a4 = re.findall(r'airbus', b)
		a5 = re.findall(r'Airbus', b)
		a6 = re.findall(r'AIRBUS', b)
		a61 = re.findall(r'самолет', b)
		a62 = re.findall(r'аэробус', b)
		a7 = len(a1) + len(a2) + len(a3) + len(a4) + len(a5) + len(a6) + len(a61) + len(a62)
		bo1 = re.findall(r'boat', b)
		bo2 = re.findall(r'Boat', b)
		bo3 = re.findall(r'BOAT', b)
		bo31 = re.findall(r'ship', b)
		bo32 = re.findall(r'Ship', b)
		bo33 = re.findall(r'SHIP', b)
		bo34 = re.findall(r'лодка', b)
		bo4 = len(bo1) + len(bo2) + len(bo3) + len(bo31) + len(bo32) + len(bo33) + len(bo34)
		mo1 = re.findall(r'motorcycle', b)
		mo2 = re.findall(r'Motorcycle', b)
		mo3 = re.findall(r'MOTORCYCLE', b)
		mo31 = re.findall(r'motor', b)
		mo32 = re.findall(r'Motor', b)
		mo33 = re.findall(r'MOTOR', b)
		mo34 = re.findall(r'мотоцикл', b)
		mo35 = re.findall(r'мотор', b)
		mo36 = re.findall(r'Мопеды', b)
		mo4 = len(mo1) + len(mo2) + len(mo3) + len(mo31) + len(mo32) + len(mo33) + len(mo34) + len(mo35) + len(mo36)
		c1 = re.findall(r'car', b)
		c2 = re.findall(r'Car', b)
		c22 = re.findall(r'CAR', b)
		c111 = re.findall(r'автомобиль', b)
		c3 = len(c1) + len(c2) + len(c22) + len(c111)
		c41 = re.findall(r'carousel', b)
		c5 = re.findall(r'carry', b)
		c222 = re.findall(r'Carry', b)
		c223 = re.findall(r'CARRY', b)
		c224 = re.findall(r'Carousel', b)
		c55 = len(c41) + len(c5) + len(c222) + len(c223) + len(c224)
		c6 = int(c3) - int(c55)
		if (t3 > b6) and (t3 > tr4) and (t3 > by4) and (t3 > a7) and (t3 > bo4) and (t3 > mo4) and (t3 > c6):
			print(str(count) + ' This is definitely a train')
			f = open("h2.txt", "a")
			f.write(str(count) + ' This is definitely a train')
			f.write("\n")
			f.close()
		if (b6 > t3) and (b6 > tr4) and (b6 > by4) and (b6 > a7) and (b6 > bo4) and (b6 > mo4) and (b6 > c6):
			print(str(count) + ' This is definitely a bus')
			f = open("h2.txt", "a")
			f.write(str(count) + ' This is definitely a bus')
			f.write("\n")
			f.close()
		if (tr4 > b6) and (tr4 > t3) and (tr4 > by4) and (tr4 > a7) and (tr4 > bo4) and (tr4 > mo4) and (tr4 > c6):
			print(str(count) + ' This is definitely a truck')
			f = open("h2.txt", "a")
			f.write(str(count) + ' This is definitely a truck')
			f.write("\n")
			f.close()
		if (by4 > b6) and (by4 > tr4) and (by4 > t3) and (by4 > a7) and (by4 > bo4) and (by4 > mo4) and (by4 > c6):
			print(str(count) + ' This is definitely a bicycle')
			f = open("h2.txt", "a")
			f.write(str(count) + ' This is definitely a bicycle')
			f.write("\n")
			f.close()
		if (a7 > b6) and (a7 > tr4) and (a7 > by4) and (a7 > t3) and (a7 > bo4) and (a7 > mo4) and (a7 > c6):
			print(str(count) + ' This is definitely a airplane')
			f = open("h2.txt", "a")
			f.write(str(count) + ' This is definitely a airplane')
			f.write("\n")
			f.close()
		if (bo4 > t3) and (bo4 > b6) and (bo4 > tr4) and (bo4 > by4) and (bo4 > a7) and (bo4 > mo4) and (bo4 > c6):
			print(str(count) + ' This is definitely a boat')
			f = open("h2.txt", "a")
			f.write(str(count) + ' This is definitely a boat')
			f.write("\n")
			f.close()
		if (mo4 > t3) and (mo4 > b6) and (mo4 > tr4) and (mo4 > by4) and (mo4 > a7) and (mo4 > bo4) and (mo4 > c6):
			print(str(count) + ' This is definitely a motorcycle')
			f = open("h2.txt", "a")
			f.write(str(count) + ' This is definitely a motorcycle')
			f.write("\n")
			f.close()
		if (c6 > t3) and (c6 > b6) and (c6 > tr4) and (c6 > by4) and (c6 > a7) and (c6 > bo4) and (c6 > mo4):
			print(str(count) + ' This is definitely a car')
			f = open("h2.txt", "a")
			f.write(str(count) + ' This is definitely a car')
			f.write("\n")
			f.close()
		if '<div class="captcha__play-image"></div><div class="captcha__play-text">' in b:
			hc_solver(filePath, count)
	except (KeyError, requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError, requests.exceptions.ProxyError, json.decoder.JSONDecodeError):
		hc_solver(filePath, count)
headers = {'Cookie': '__cfduid=d8965dc10b7df208178bf5fa320f8f1301612626370; INGRESSCOOKIE=1612625839.393.66.50185; __cflb=0H28vk2VKwPbLoawEwCcxX8CVxVs3EjBjiBGQK5JpzQ; hmt_id=80dfb247-0523-4733-b7b4-ccebc3e02d80'}
lines2 = []
count = 4
with open('hc.txt') as f:
	data = json.loads(f.read())
	dd = data["tasklist"]
	count1 = range(0, len(dd))
for x in count1:
	dd = data["tasklist"]
	d = dd[x]
	d2 = d['datapoint_uri']
	lines2.append(d2)
for b in range(4, 9):
	a = lines2[b]
	u1 = a.replace('https://imgs.hcaptcha.com/','')
	u1 = u1.replace('/','')
	filePath1 = u1.replace('\\','')
	filePath1 = filePath1.replace('//','')
	filePath1 = filePath1.replace('\\\\','')
	filePath = filePath1 + '.jpg'
	hc_solver(filePath, count)
	count+=1
