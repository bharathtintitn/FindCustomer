import re
from re import sub
import time
import cookielib
from cookielib import CookieJar
import urllib2
from urllib2 import urlopen

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')]

keyWord = 'bharath'

startingLink = 'https://twitter.com/search/realtime?q='

def main():
	try:

		sourceCode = opener.open(startingLink +keyWord+'&src=hash').read()
		#print sourceCode
		print len(sourceCode)

		splitSource = re.findall(r'<p class="js-tweet-text tweet-text">(.*?)</p>',sourceCode)
		print "len is ", len(splitSource)
		for item in splitSource:
			print item
			time.sleep(555)

	except Exception, e:
		print str(e)
		print "its in error"
		

main()
