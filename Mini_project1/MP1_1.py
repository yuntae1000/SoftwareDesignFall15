#from pattern.web import*

#oliver_twist_full_text=URL('http://www.gutenberg.org/ebooks/730.txt.utf-8').download()
#print oliver_twist_full_text


# import pickle
# f= open('oliver_twist.pickle','w')
# pickle.dump(oliver, f)
# f.close()
# input_file= open('oliver_twist', 'r')
# reloaded_copy_of_texts= pickle.load(input_file)

from pattern.web import Google, Bing
from pattern.web import Yahoo
from pattern.web import SEARCH

import indicoio
indicoio.config.api_key = '8d05933c4c2ca769d1e064dfbea1fe8a'
a={}
a=indicoio.political("Those who surrender freedom for security will not have, nor do they deserve, either one.")
print a['Green']
rawurl_nyt=[]
rawurl_cbs=[]
rawurl_wsj=[]
rawurl_fox=[]

g=Google()
#g.pages=5
#g=Bing()
print g

#New York Times url get
for i in range(1,4):

	for result in g.search('democrat and republican site:nytimes.com', start=i):
	   
	    print result.url
	    rawurl_nyt.append(result.url)
	   
print rawurl_nyt
print len(rawurl_nyt)
f_nyt=open("url_nyt.txt", "w")
print >>f_nyt, rawurl_nyt
f_nyt.close()

########################
##cbs news url
for i in range(1,4):

	for result in g.search('democrat and republican  site:cbsnews.com', start=i):
	    #print result
	    print result.url
	    rawurl_cbs.append(result.url)
	    
print rawurl_cbs
f_cbs=open("url_cbs.txt", "w")
print >>f_cbs, rawurl_cbs
f_cbs.close()


########################
##wallstreet journal url
for i in range(1,4):

	for result in g.search('democrat and republican  site:wsj.com', start=i):
	    #print result
	    print result.url
	    rawurl_wsj.append(result.url)
	    
print rawurl_wsj
print len(rawurl_wsj)
f_wsj=open("url_wsj.txt", "w")
print >>f_wsj, rawurl_wsj
f_wsj.close()

########################
##fox news url
for i in range(1,4):

	for result in g.search('democrat and republican site:foxnews.com', start=i):
	    #print result
	    print result.url
	    rawurl_fox.append(result.url)
	    
print rawurl_fox
f_fox=open("url_fox.txt", "w")
print >>f_fox, rawurl_fox
f_fox.close()






