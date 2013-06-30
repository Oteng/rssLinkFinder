
import urllib2
from bs4 import BeautifulSoup

class openUrl(object):
	"""for opening and getting data at the url"""
	def __init__(self, url):
		super(openUrl, self).__init__()
		self.url = url
	def open(self):
		""" return a file like object containing the 
			data at the url """
		try:
			content = urllib2.urlopen(urllib2.Request(self.checkUrl(self.url),
								headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:10.0) Gecko/20100101 Firefox/10.0'}))
		except Exception, e:
			print e
			return None
		return content
		
	def checkUrl(self,url):
		""" to allow user to not to enter http 
			return url with http """
		if (url[:7] != 'http://') and (url[:8] != 'https://'):
			tempUrl = 'http://'
			return tempUrl + url
		elif (url[:8] == 'http://') or (url[:9] == 'https://'):
			return url
	def setUrl(self, url):
		""" change the current url """
		self.url = url
	def getUrl(self):
		""" get the current url """
		return self.url

class rssLinkFinder(object):
	"""parse the file returned by openUrl and returns a list of tuples containing
	   the tile and rss links in the page"""
	def __init__(self, urlFile):
		super(rssLinkFinder, self).__init__()
		self.urlFile = urlFile
		self.urlContent = self.urlFile.read()

	def parse(self,tag):
		""" return an object of the tag
			tag = string """
		self.soup = BeautifulSoup(self.urlContent)
		self.Tags = self.soup.find_all(tag)
		return self.Tags
	
	def getRssLink(self):
		""" loop over tags and get tags with rss type and 
			return a list containing tuples of title or none and href or none """
		temp = []
		listATag = self.parse('a')
		for i in listATag:
			if i.get('type') == 'application/rss+xml':
				temp.append((i.get('title'),i.get('href')))
		listLinkTag = self.parse('link')
		for i in listLinkTag:
			if i.get('type') == 'application/rss+xml':
				temp.append((i.get('title'),i.get('href')))
		return temp