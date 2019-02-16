import requests
import os, sys, time

def banner():
	print (""+O+"")
	print ("""

GHOSTBLACK
╦═╗╔═╗╦  ╦╔═╗╦═╗╔═╗╔═╗╔═╗╦╔═  ╦╔═╗ c0d3d by : Zekkel AR
╠╦╝║╣ ╚╗╔╝║╣ ╠╦╝╔═╝║╣ ║  ╠╩╗  ║╠═╝
╩╚═╚═╝ ╚╝ ╚═╝╩╚═╚═╝╚═╝╚═╝╩ ╩  ╩╩  
FA HAXOR, Ago Oeng, Aalex, Faisal, Magrisya, Shinigami Ryuken
""")
R = '\033[31m'   # Red
N = '\033[1;37m' # White
G = '\033[32m'   # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' # Blue
C = '\033[36m' # cyan

class a:
	try:
		def __init__(self):
			print ("[*] dont use https:// or http://")
			print ("[*] Ex : Site.com")
			self.url = input("url => "+C+" ")
		def kyu(self):
			kyuraz = requests.get("https://api.hackertarget.com/reverseiplookup/?q={}".format(self.url)).text
			if "error check" in kyuraz:
				print ("dont use https:// or http:// ")
			else:
				print (""+C+"")
				print (kyuraz)
				with open('result.txt', 'w') as y:
					y.write(str(kyuraz) + '\n')	
					print (""+G+"")
					print ("Saved In result.txt")	
	except KeyboardInterrupt:
		print ("CTRL + C")


if __name__ == "__main__":
	os.system('clear')
	banner()
	zek = a()
	zek.kyu()


