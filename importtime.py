import time
import webbrowser
x = 0
while (x <3):
	webbrowser.open("www.google.com")
	time.sleep(3)
	x += 1

def somelist(delay,url):
	by = delay
	d = 0
	while (d < delay):
		webbrowser.open("url")
		time.sleep(by)
		d += 1

myurl = [[10,"www.yahoo,com"],[20,"www.google.com"],[30,"www.cashcraft.com"]]
for i in myurl:
	somelist(i[0],i[1])
	