# @@Author : Wahyu Arif P
# @@Github : https://github.com/warifp
# @@Update : 3 April 2019 3:35
# Please don't change or recode.


from urllib2 import Request, urlopen, URLError, HTTPError
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()

def randWahyuArifP(j):
	i = 0
	while i<=j:
		print " ",
		i+=1

def VerifikasiBigTokenWahyuArifP():
	input_link = open("list.txt","r");
	while True:
		linkWahyuArifP = input_link.readline()
		if not linkWahyuArifP:
			break
		reqWahyuArifP = Request(linkWahyuArifP)
		browser = webdriver.Chrome(chrome_options=chrome_options)
		browser.get(linkWahyuArifP)
		try:
			response = urlopen(reqWahyuArifP)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "Success Open => ",linkWahyuArifP
			browser.quit()
    		
def bannerWahyuArifP():
	randWahyuArifP(9); print "Open Link with List by Wahyu Arif P"

bannerWahyuArifP()
VerifikasiBigTokenWahyuArifP()
