#cord to mining the urls from google and save it to local .txt files
# using patter. to search from Google

from pattern.web import Google
# You're not using SEARCH in this file -- better not to import it
from pattern.web import SEARCH

# You're not using indicoio in this file -- better not to import it
# using indicoio for polytical and sentiment analysis
import indicoio
indicoio.config.api_key = '8d05933c4c2ca769d1e064dfbea1fe8a'

# declare arrays which save raw url mined from pattern.search
# new york times urls, cbs new urls, wallstreet journal urls, foxnew urls
rawurl_nytimes=[]
rawurl_cbsnews=[]
rawurl_wsj=[]
rawurl_foxnews=[]
journal_names=['nytimes', 'cbsnews', 'wsj', 'foxnews']
rawurls=[rawurl_nytimes, rawurl_cbsnews, rawurl_wsj, rawurl_foxnews]

g=Google()


#get the New York Times url
for journal, raw_url_title in zip(journal_names, rawurls):

	#in order to get 30 urls with the keyword, used for-loop
	for i in range(1,4):

		# search google results correspoding to the following keyword
		for result in g.search('Donald Trump opinion site:'+journal+'.com', start=i):

		    print result.url # Better not to print all of these -- they're not informative to the person using your program
		    # append the urls to the rawurl_ array
		    # ^ Not a useful comment - you're just stating what the next line does.
		    # Better to say _why_ the next line does what it does
		    raw_url_title.append(result.url)

	print raw_url_title # Again, better not to print all of these -- I'm not going to keep writing this, but it applies throughout your code
	print len(raw_url_title)

	# saves the keyword to the local file in order to reduce query
	# we will use this file for analyzing later on

	f=open('url_'+journal+'.txt', "w")
	print >>f, raw_url_title
	f.close()

# It would be better to put everything you're doing in this file into a function,
# then you can write a "master function" at the end which chains all of the steps
# in your process together
